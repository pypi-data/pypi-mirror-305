from __future__ import annotations

import hashlib
import json
import logging
from dataclasses import replace
from typing import Any, Callable, Literal, cast, overload

import lancedb
import numpy as np
import pyarrow as pa
from cachetools import TTLCache
from datasets import ClassLabel, Dataset
from pandas import DataFrame
from tqdm.auto import tqdm, trange

from orca_common.api_types import ColumnName, TableCreateMode
from orcalib.database import OrcaDatabase
from orcalib.exceptions import OrcaBadRequestException
from orcalib.orca_types import EnumT, EnumTypeHandle, ImageT, IntT, TextT, VectorT
from orcalib.orcadb_url import OrcaServerLocation, is_url, parse_orcadb_url
from orcalib.rac_util import format_dataset

from .embedding_models import EmbeddingModel, EmbeddingTrainingArguments
from .memory_types import DatasetLike, InputType, LabeledMemory, LabeledMemoryLookup
from .memoryset_analysis import LabeledMemorysetAnalysisResults
from .reranker import (
    MemoryPairsDataset,
    Reranker,
    RerankerTrainingArguments,
    SharedEncoderReranker,
)
from .util import (
    MemoryLookupResults,
    MemoryToInsert,
    bytes_to_pil_image,
    format_lookup_results,
    transform_data_to_dict_list,
    transform_rows_to_labeled_memories,
)

# 2 weeks in seconds
CACHE_TTL = 1.21e6


def _get_embedding_hash(q: np.ndarray) -> str:
    query_bytes = q.tobytes()
    hash_obj = hashlib.sha256()
    hash_obj.update(query_bytes)
    return hash_obj.hexdigest()


class LabeledMemoryset:  # TODO (2): metaclass this so we can split out the implementations of local and hosted into separate classes
    """
    Collection of memories with labels that are stored in an OrcaDB table and can be queried using embedding similarity search.
    """

    # TODO(p2): `adapt` method to change embedding models (i.e. re-compute embeddings for the entire dataset with a new model)

    def _init_local_db(self):
        """Initializes a local (embedded!) database for storing memories and their embeddings."""
        # TODO: optimize vector index a bit incl supporting CUDA where available (lance has cuda support)

        assert isinstance(self.db, lancedb.DBConnection) and self.mode == "local"

        # first create meta table if it doesn't exist and check that the model and version match if it does
        if f"rac_meta_{self.table_name}" not in self.db.table_names():
            meta_table = self.db.create_table(
                f"rac_meta_{self.table_name}",
                schema=pa.schema(
                    [
                        pa.field("model", pa.string()),
                        pa.field("model_version", pa.string()),
                        pa.field("dummy_vector", pa.list_(pa.float32(), list_size=1)),
                    ]
                ),
            )

        meta_table = self.db.open_table(f"rac_meta_{self.table_name}")
        meta_rows = meta_table.to_pandas()

        if meta_table.count_rows() == 0:
            meta_table.add(
                [
                    {
                        "model": self.embedding_model.name,
                        "model_version": f"{self.embedding_model.version}",
                        "dummy_vector": [1.0],
                    }
                ]
            )
        elif meta_table.count_rows() > 1:
            raise ValueError(
                f"Multiple rows found for table {self.table_name}. Memoryset only supports one model version per table."
            )
        elif meta_table.count_rows() == 1 and (
            meta_rows["model"].iloc[0] != self.embedding_model.name
            or meta_rows["model_version"].iloc[0] != f"{self.embedding_model.version}"
        ):
            raise ValueError(
                f"Model or model version mismatch for existing Memoryset: {self.embedding_model.name}, version: {self.embedding_model.version} != {meta_rows['model'].iloc[0]}, version: {meta_rows['model_version'].iloc[0]}"
            )

        # create table if it doesn't exist
        if self.table_name not in self.db.table_names():
            _memoryset_schema = pa.schema(
                [
                    pa.field("text", pa.string()),
                    pa.field("image", pa.binary()),
                    pa.field("label", pa.int64()),
                    pa.field("label_name", pa.string()),
                    pa.field("metadata", pa.string()),
                    pa.field("memory_version", pa.int64()),
                    pa.field(
                        "embedding",
                        pa.list_(pa.float32(), list_size=self.embedding_model.embedding_dim),
                    ),
                ]
            )

            self.db.create_table(self.table_name, schema=_memoryset_schema, exist_ok=True)
            # TODO: add vector index (for more speed - works without it but is slow)

    def _init_hosted_db(self):
        """Initializes a hosted database (OrcaDB cloud or localhost) for storing memories and their embeddings."""

        assert isinstance(self.db, OrcaDatabase) and self.mode == "hosted"

        meta_table = self.db.create_table(
            f"rac_meta_{self.table_name}",
            model=TextT,
            model_version=TextT,
            if_table_exists=TableCreateMode.RETURN_CURR_TABLE,
        )
        meta_rows = cast(
            list[dict[ColumnName, Any]], meta_table.select().fetch()
        )  # We know the type b/c include_ids is False
        if len(meta_rows) == 0:
            meta_table.insert({"model": self.embedding_model.name, "model_version": f"{self.embedding_model.version}"})
        elif len(meta_rows) > 1:
            raise ValueError(
                f"Multiple rows found for table {self.table_name}. Memoryset only supports one model version per table."
            )
        elif len(meta_rows) == 1 and (
            meta_rows[0]["model"] != self.embedding_model.name
            or meta_rows[0]["model_version"] != f"{self.embedding_model.version}"
        ):
            raise ValueError(
                f"Model or model version mismatch for existing Memoryset: {self.embedding_model.name}, version: {self.embedding_model.version} != {meta_rows[0]['model']}, version: {meta_rows[0]['model_version']}"
            )

    mode: Literal["local", "hosted"]

    def __init__(
        self,
        uri: str | None = None,
        api_key: str | None = None,
        secret_key: str | None = None,
        database: str | None = None,
        table: str | None = None,
        embedding_model: EmbeddingModel = EmbeddingModel.GTE_BASE,
        reranker: Reranker | None = None,  # TODO: make this a reranker model enum class instead
    ):
        """
        Create a new LabeledMemoryset.

        Note:
            This will create a database if it doesn't exist yet and a table in it.

        Args:
            uri: URL of the database that should store the memories table or name of the table for
                the memories. Either a file URL or the URL to a hosted OrcaDB instance is accepted.
                If empty, the `ORCADB_URL` environment variable is used instead. If a string is
                provided, it is interpreted as the name of the table to create in the database
                specified by the `ORCADB_URL` environment variable.
            api_key: API key for the OrcaDB instance. If not provided, the `ORCADB_API_KEY`
                environment variable or the credentials encoded in the uri are used
            secret_key: Secret key for the OrcaDB instance. If not provided, the `ORCADB_SECRET_KEY`
                environment variable or the credentials encoded in the uri are used.
            database: Name of the database. Do not provide this if it is already encoded in the `uri`.
            table: Name of the table. Do not provide this if it is already encoded in the `uri`.
            embedding_model: Embedding model to use for semantic similarity search.
            reranker: optional reranking model to use during lookup.

        Examples:
            Infer connection details from the ORCADB_URL, ORCADB_API_KEY, and ORCADB_SECRET_KEY environment variables:

            >>> import os
            >>> os.environ["ORCADB_URL"] = "https://<my-api-key>:<my-secret-key>@instance.orcadb.cloud/my-db"
            >>> LabeledMemoryset()
            LabeledMemoryset(table="memories", database="my-db")
            >>> LabeledMemoryset("my_memories_table")
            LabeledMemoryset(table="my_memories_table", database="my-db")

            All connection details can be fully encoded in the the uri:

            >>> LabeledMemoryset("https://<my-api-key>:<my-secret-key>@instance.orcadb.cloud/my-db/my-memories-table")
            LabeledMemoryset(table="my-memories-table", database="my-db")

            Or they can be provided explicitly:

            >>> LabeledMemoryset(
            ...    "https://instance.orcadb.cloud",
            ...    api_key="my-api-key",
            ...    secret_key="my-secret-key",
            ...    database="my-db",
            ...    table="my-memories-table"
            ... )
            LabeledMemoryset(table="my-memories-table", database="my-db")
        """
        self.table = None
        self.index = None
        self.embedding_model = embedding_model
        self.reranker = reranker
        self.cache = TTLCache(maxsize=25000, ttl=CACHE_TTL)

        self._location = parse_orcadb_url(
            uri if is_url(uri) else None,
            api_key=api_key,
            secret_key=secret_key,
            database=database,
            table=table if is_url(uri) else (table or uri),
        )
        if not self._location.table:
            self._location.table = "memories"
        self.url = self._location.url
        self.table_name = self._location.table
        if isinstance(self._location, OrcaServerLocation):
            self.mode = "hosted"
            self.database_name = self._location.database
            self.db = OrcaDatabase(
                self._location.base_url,
                api_key=self._location.api_key,
                secret_key=self._location.secret_key,
                name=self._location.database,
            )
            self._init_hosted_db()
        else:
            self.mode = "local"
            self.path = self._location.path
            self.db = lancedb.connect(self.path)
            self._init_local_db()

    def _insert_local(self, data: list[MemoryToInsert]):
        assert self.mode == "local" and isinstance(self.db, lancedb.DBConnection)
        if len(data) > 0:
            self.db.open_table(self.table_name).add(data)

    def _insert_hosted(self, data: list[MemoryToInsert], label_col_type: EnumTypeHandle | None = None):
        assert self.mode == "hosted" and isinstance(self.db, OrcaDatabase)

        if not self.table:
            self.table = self.db.create_table(
                self.table_name,
                text=TextT,
                image=ImageT["PNG"],  # type: ignore -- ImageT takes a format param
                memory_version=IntT,
                label=label_col_type or IntT,
                label_name=TextT,
                metadata=TextT,
                embedding=VectorT[self.embedding_model.embedding_dim],
                if_table_exists=TableCreateMode.RETURN_CURR_TABLE,
            )
            self.index = self.db.create_vector_index(
                index_name=f"{self.table_name}_embedding_index",
                table_name=self.table_name,
                column="embedding",
                error_if_exists=False,
            )
            if self.index is None:
                logging.info(f"Using existing {self.table_name}_embedding_index")
                self.index = self.db.get_index(f"{self.table_name}_embedding_index")

        # table.insert takes in list of dicts and we must leave off image if there is no data for it or we will get an error
        data_to_insert = [cast(dict, mem) for mem in data]
        for mem in data_to_insert:
            if mem["image"] is None:
                del mem["image"]
        self.table.insert(data_to_insert)

    def insert(
        self,
        dataset: DatasetLike,
        log: bool = True,
        compute_embeddings: bool = True,
        batch_size: int = 32,
        only_if_empty: bool = False,
    ):
        """
        Inserts a dataset into the LabeledMemoryset database.

        For dict-like or list of dict-like datasets, there must be a `label` key and one of the following keys: `text`, `image`, or `value`.
        If there are only two keys and one is `label`, the other will be inferred to be `value`.

        For list-like datasets, the first element of each tuple must be the value and the second must be the label.

        Args:
            dataset: data to insert into the memoryset
            log: whether to show a progressbar and log messages
            compute_embeddings: whether to compute embeddings for the dataset or take them from the dataset
            batch_size: the batch size when creating embeddings from memories
            only_if_empty: whether to skip the insert if the memoryset is not empty
        Examples:
            # Example 1: Inserting a dictionary-like dataset
            >>> dataset = [{
            ...    "text": "text 1",
            ...    "label": 0
            ... }]
            >>> memoryset = LabeledMemoryset("file:///path/to/memoryset")
            >>> memoryset.insert(dataset)

            # Example 2: Inserting a list-like dataset
            >>> dataset = [
            ...    ("text 1", 0),
            ...    ("text 2", 1)
            ]
            >>> memoryset = LabeledMemoryset("file:///path/to/memoryset")
            >>> memoryset.insert(dataset)

            # Example 3: Inserting a Hugging Face Dataset
            from datasets import Dataset
            >>> dataset = load_dataset("frgfm/imagenette", "320px")
            >>> memoryset = LabeledMemoryset("file:///path/to/memoryset")
            >>> memoryset.insert(dataset)
        """
        if len(self) and only_if_empty:
            logging.warning("Skipping insert: `only_if_empty` is True and memoryset is not empty.") if log else None
            return
        transformed_data = transform_data_to_dict_list(dataset, self.mode)
        if len(transformed_data) > 0 and "text" in transformed_data[0]:
            # This sorts the data by text length so that batches are created from similar length samples
            # This smaller amount of added padding decreases overall computational complexity.
            transformed_data = sorted(transformed_data, key=lambda x: -len(x["text"]) if x["text"] is not None else 0)

        if compute_embeddings:
            # Add embeddings to the transformed data
            embeddings = self.embedding_model.embed(
                cast(
                    list[InputType],
                    [
                        mem["text"]
                        or (bytes_to_pil_image(mem["image"]) if isinstance(mem["image"], bytes) else mem["image"])
                        for mem in transformed_data
                    ],
                ),
                show_progress_bar=log,
                batch_size=batch_size,
            )
            for item, embedding in zip(transformed_data, embeddings):
                item["embedding"] = embedding.tolist()
        else:
            if not all(item["embedding"] is not None for item in transformed_data):
                raise ValueError("Embedding must be provided if compute_embeddings is False.")

        if self.mode == "local":
            self._insert_local(transformed_data)
        elif self.mode == "hosted":
            label_col_type = (
                EnumT[dataset.features["label"].names]
                if isinstance(dataset, Dataset) and isinstance(dataset.features["label"], ClassLabel)
                else None
            )
            self._insert_hosted(transformed_data, label_col_type=label_col_type)
        else:
            raise Exception("Memoryset not initialized correctly")

    def _lookup_local(
        self, query: np.ndarray, k: int, column_oriented: bool | None = False, log: bool = False
    ) -> list[list[LabeledMemoryLookup]] | list[MemoryLookupResults]:
        assert self.mode == "local"

        def single_lookup(q: np.ndarray) -> list[LabeledMemoryLookup] | MemoryLookupResults:
            assert isinstance(self.db, lancedb.DBConnection)

            cache_key = (_get_embedding_hash(q), k)
            result = self.cache.get(cache_key, None)

            if result is None:
                result = self.db.open_table(self.table_name).search(q).with_row_id(True).limit(k).to_list()
                self.cache[cache_key] = result

                if column_oriented:
                    column_oriented_result: MemoryLookupResults = {
                        "value": [],
                        "embedding": [],
                        "memory_id": [],
                        "memory_version": [],
                        "label": [],
                        "label_name": [],
                        "metadata": [],
                        "lookup_score": [],
                    }
                    for row in result:
                        metadata = json.loads(row["metadata"]) if row["metadata"] is not None else {}
                        if row["image"] is not None:
                            value = bytes_to_pil_image(row["image"])
                        else:
                            value = row["text"]
                        column_oriented_result["value"].append(value)
                        column_oriented_result["embedding"].append(np.array(row["embedding"]))
                        column_oriented_result["memory_id"].append(row["_rowid"])
                        column_oriented_result["memory_version"].append(row["memory_version"])
                        column_oriented_result["label"].append(row["label"])
                        column_oriented_result["label_name"].append(row["label_name"])
                        column_oriented_result["metadata"].append(metadata)
                        column_oriented_result["lookup_score"].append(np.dot(q, np.array(row["embedding"])))
                    return column_oriented_result

            memories = []
            for row in result:
                metadata = json.loads(row["metadata"]) if row["metadata"] is not None else {}
                if row["image"] is not None:
                    value = bytes_to_pil_image(row["image"])
                else:
                    value = row["text"]
                memories.append(
                    LabeledMemoryLookup(
                        value=value,
                        embedding=np.array(row["embedding"]),
                        memory_id=row["_rowid"],
                        memory_version=row["memory_version"],
                        label=row["label"],
                        label_name=row["label_name"],
                        metadata=metadata,
                        lookup_score=np.dot(q, np.array(row["embedding"])),  # Calculate inner product
                    )
                )
            return memories

        if len(query.shape) == 1:
            return (
                cast(list[MemoryLookupResults], [single_lookup(query)])
                if column_oriented
                else cast(list[list[LabeledMemoryLookup]], [single_lookup(query)])
            )

        # For some reason, all_results: list[list[LabeledMemory]] | list[MemoryLookupResults] = [] is not typing the variable correctly
        # so we have to cast it to the correct type
        all_results = cast(list[list[LabeledMemoryLookup]] | list[MemoryLookupResults], [])
        for q in tqdm(query, disable=(not log) or (len(query) <= 100)):
            all_results.append(single_lookup(q))  # type: ignore -- we know that all return types will be the same
        return (
            cast(list[MemoryLookupResults], all_results)
            if column_oriented
            else cast(list[list[LabeledMemoryLookup]], all_results)
        )

    def _lookup_hosted(
        self,
        query: np.ndarray,
        k: int,
        batch_size: int = 32,
        run_ids: list[int] | None = None,
        column_oriented: bool | None = False,
        log: bool = False,
    ) -> list[list[LabeledMemoryLookup]] | list[MemoryLookupResults]:
        assert self.mode == "hosted" and isinstance(self.db, OrcaDatabase)
        if self.table is None:
            try:
                self.table = self.db.get_table(self.table_name)
            except ValueError:
                raise ValueError(
                    f"Table '{self.table_name}' not found in database '{self.database_name}'. Please call insert to create table and add data."
                )
        if self.index is None:
            try:
                self.index = self.db.get_index(f"{self.table_name}_embedding_index")
            except OrcaBadRequestException:
                raise ValueError(
                    f"Index '{self.table_name}_embedding_index' not found in table '{self.table_name}'. Please call insert first to create the index."
                )

        if len(query.shape) == 1:
            query_list = [(0, query)]
        else:
            query_list = [(idx, q) for idx, q in enumerate(query)]

        # save results in a list of tuples where the first element is the query index and the second element is the result
        all_results: list[tuple[int, list]] = []

        # run_ids are only set if we have enabled curate tracking in which case caching is not possible
        if not run_ids:
            for q in query_list:
                cache_key = (_get_embedding_hash(q[1]), k)
                result = self.cache.get(cache_key, None)
                if result is not None:
                    all_results.append((q[0], result))
                    query_list.remove(q)

        for i in trange(0, len(query_list), batch_size, disable=(not log) or (len(query_list) <= 5 // batch_size)):
            batch = query_list[i : i + (batch_size or len(query_list))]
            batch_list = [q[1].tolist() for q in batch]
            index_query = self.index.vector_scan(batch_list).select(
                "metadata",  # 0
                "image",  # 1
                "text",  # 2
                "label",  # 3
                "label_name",  # 4
                "memory_version",  # 5
                "$embedding",  # 6
                "$row_id",  # 7
            )
            if run_ids:
                batch_run_ids = run_ids[i : i + (batch_size or len(query_list))]
                index_query = index_query.track_with_curate(batch_run_ids, "rac_lookup")

            r = index_query.fetch(k).to_list()

            for idx, row in enumerate(r):
                cache_key = (_get_embedding_hash(batch[idx][1]), k)
                self.cache[cache_key] = row
                all_results.append((batch[idx][0], row))

        all_results.sort(key=lambda x: x[0])
        results = [format_lookup_results(r, query[r[0]], column_oriented=column_oriented) for r in all_results]
        return (
            cast(list[MemoryLookupResults], results)
            if column_oriented
            else cast(list[list[LabeledMemoryLookup]], results)
        )

    @overload
    def lookup(
        self,
        query: InputType | list[InputType] | np.ndarray,
        *,
        column_oriented: Literal[False] | None = False,
        k: int = 1,
        batch_size: int = 32,
        run_ids: list[int] | None = None,
        rerank: bool | None = None,
        log: bool = False,
    ) -> list[list[LabeledMemoryLookup]]:
        pass

    @overload
    def lookup(
        self,
        query: InputType | list[InputType] | np.ndarray,
        *,
        column_oriented: Literal[True],
        k: int = 1,
        batch_size: int = 32,
        run_ids: list[int] | None = None,
        rerank: bool | None = None,
        log: bool = False,
    ) -> list[MemoryLookupResults]:
        pass

    def lookup(
        self,
        query: InputType | list[InputType] | np.ndarray,
        *,
        column_oriented: bool | None = False,
        k: int = 1,
        batch_size: int = 32,
        run_ids: list[int] | None = None,
        rerank: bool | None = None,
        log: bool = False,
    ) -> list[list[LabeledMemoryLookup]] | list[MemoryLookupResults]:
        """
        Retrieves the most similar memories to the query from the memoryset.

        Args:
            query: The query to retrieve memories for. Can be a single value, a list of values, or a numpy array with value embeddings.
            k: The number of memories to retrieve.
            batch_size: The number of queries to process at a time.
            run_ids: A list of run IDs to track with the lookup.
            rerank: Whether to rerank the results. If None (default), results will be reranked if a reranker is attached to the Memoryset.
            log: Whether to log the lookup process and show progress bars.

        Returns:
            A list of lists of LabeledMemoryLookups, where each inner list contains the k most similar memories to the corresponding query.

        Examples:
            # Example 1: Retrieving the most similar memory to a single example
            >>> memoryset = LabeledMemoryset("file:///path/to/memoryset")
            >>> query = "Apple"
            >>> memories = memoryset.lookup(query, k=1)
            [
                [
                    LabeledMemoryLookup(
                        value='Orange',
                        memory_id=12,
                        memory_version=1,
                        label=0,
                        label_name='fruit',
                        embedding=array([...], dtype=float32),
                        metadata=None,
                        lookup_score=.98,
                        reranker_score=None,
                        reranker_embedding=None
                    )
                ]
            ]
        """
        # TODO (p2): allow for some retrieval config to be passed in
        if isinstance(query, InputType) or isinstance(query, list):
            embedded_query = self.embedding_model.embed(query)
        elif isinstance(query, np.ndarray):
            embedded_query = query
        else:
            raise ValueError("Query must be a single value, a list of values, or a numpy array")

        assert (
            len(embedded_query.shape) == 2 or len(embedded_query.shape) == 1
        ), "Query embedding is not in a valid shape"

        if len(embedded_query.shape) == 1:
            assert (
                embedded_query.shape[0] == self.embedding_model.embedding_dim
            ), f"Query embedding shape: {embedded_query.shape} does not match model embedding dimension: {self.embedding_model.embedding_dim}"
        else:
            assert (
                embedded_query.shape[1] == self.embedding_model.embedding_dim
            ), f"Query embedding shape: {embedded_query.shape} does not match model embedding dimension: {self.embedding_model.embedding_dim}"
        # Default reranking to `True` if a reranker is attached and to `False` otherwise.
        rerank = rerank or (rerank is None and self.reranker is not None)
        if rerank:
            if not self.reranker:
                raise ValueError("rerank is set to true but no reranker model has been set on this memoryset")
            k = k * self.reranker.compression
        if self.mode == "local":
            memory_lookups = self._lookup_local(embedded_query, k=k, column_oriented=column_oriented, log=log)
        elif self.mode == "hosted":
            memory_lookups = self._lookup_hosted(
                embedded_query, k=k, batch_size=batch_size, run_ids=run_ids, column_oriented=column_oriented, log=log
            )
        else:
            raise Exception("Memoryset not initialized correctly")

        # TODO: support reranking for column-oriented results
        if rerank and not column_oriented:
            assert self.reranker is not None
            # we know this is a list of list of LabeledMemoryLookups because we check that column_oriented is False
            memory_lookups = cast(list[list[LabeledMemoryLookup]], memory_lookups)
            if isinstance(query, str):
                queries_list = [query]
            else:
                if not isinstance(query, list) or not isinstance(query[0], str):
                    raise ValueError("reranking only works when passing a string as the query")
                queries_list = cast(list[str], query)
            # TODO: use cached reranker embeddings if available
            reranked_results = [
                self.reranker.rerank(q, memories=[cast(str, m.value) for m in ms], top_k=k)
                for q, ms in zip(queries_list, memory_lookups)
            ]
            return [
                [
                    LabeledMemoryLookup(
                        reranker_score=reranked_results[j].scores[idx], **memory_lookups[j][idx].__dict__
                    )
                    for idx in reranked_results[j].indices
                ]
                for j in range(len(reranked_results))
            ]
        return memory_lookups

    def to_list(self, limit: int | None = None) -> list[LabeledMemory]:
        """
        Get a list of all the memories in the memoryset.

        Returns:
            list containing the memories
        """
        if self.mode == "local" and isinstance(self.db, lancedb.DBConnection):
            return transform_rows_to_labeled_memories(
                # TODO: with_row_id does not actually work https://github.com/lancedb/lancedb/issues/1724
                self.db.open_table(self.table_name)
                .search()
                .with_row_id(True)
                .limit(limit)
                .to_list()
            )
        elif self.mode == "hosted" and isinstance(self.db, OrcaDatabase) and self.table:
            return transform_rows_to_labeled_memories(
                cast(list[tuple[int, dict[ColumnName, Any]]], self.table.select().fetch(limit=limit, include_ids=True))
            )
        else:
            raise Exception("Memoryset not initialized correctly")

    def to_pandas(self, limit: int | None = None) -> DataFrame:
        """
        Get a [DataFrame][pandas.DataFrame] representation of the memoryset.

        Returns:
            DataFrame containing the memories
        """
        return DataFrame(self.to_list(limit))

    def to_dataset(self, limit: int | None = None) -> Dataset:
        return Dataset.from_pandas(self.to_pandas(limit))

    def __getitem__(self, idx: int) -> LabeledMemory:
        return self.to_list()[idx]

    def __len__(self) -> int:
        if self.mode == "local" and isinstance(self.db, lancedb.DBConnection):
            return self.db.open_table(self.table_name).count_rows()
        elif self.mode == "hosted" and isinstance(self.db, OrcaDatabase):
            return self.db[self.table_name].count() if self.table_name in self.db else 0
        else:
            raise Exception("Memoryset not initialized correctly")

    @property
    def num_rows(self) -> int:
        return len(self)

    def _get_reset_destination_memoryset(
        self, destination: LabeledMemoryset | str | None, embedding_model: EmbeddingModel | None = None
    ) -> LabeledMemoryset:
        """Gets destination memoryset, RESETS THE DESTINATION MEMORYSET IF IT ALREADY EXISTS"""
        # If destination is None or matches self, return self
        if destination is None or (
            (isinstance(destination, LabeledMemoryset) and destination.url == self.url)
            or ((isinstance(destination, str) and (destination == self.url or destination == self.table_name)))
        ):
            destination = self
            if embedding_model is not None:
                destination.embedding_model = embedding_model
        elif isinstance(destination, str):
            if not is_url(destination):
                self.drop_table(destination)
            destination = LabeledMemoryset(
                destination if is_url(destination) else self.url.split("#")[0],
                table=None if is_url(destination) else destination,
                api_key=(
                    self._location.api_key
                    if self.mode == "hosted" and isinstance(self._location, OrcaServerLocation)
                    else None
                ),
                secret_key=(
                    self._location.secret_key
                    if self.mode == "hosted" and isinstance(self._location, OrcaServerLocation)
                    else None
                ),
                embedding_model=self.embedding_model if embedding_model is None else embedding_model,
                reranker=self.reranker,
            )

        destination.reset()
        return destination

    def update_embedding_model(
        self, embedding_model: EmbeddingModel, destination: LabeledMemoryset | str | None = None
    ) -> LabeledMemoryset:
        """
        Updates the embedding model for the memoryset and re-embeds all memories in the current
        memoryset or a new destination memoryset if it is provided.

        Note:
            This will reset the destination memoryset if it already exists.

        Args:
            embedding_model: new embedding model to use.
            destination: destination memoryset to store the results in, this can either be
                a memoryset instance, or the URL to a new memoryset, or the name of a table in the
                same database. A table for the destination will be created if it does not already
                exist. It this is `None` the current memoryset will be updated.

        Returns:
            The destination memoryset with the updated embeddings.

        Examples:
            Replace the embedding model for the current memoryset:
            >>> memoryset = LabeledMemoryset("file:./orca.db#my_memoryset")
            >>> memoryset.update_model(EmbeddingModel.CLIP_BASE)

            Create a new memoryset with a new embedding model:
            >>> memoryset = LabeledMemoryset("file:./orca.db#my_memoryset")
            >>> new_memoryset = memoryset.update_model(EmbeddingModel.CLIP_BASE, "my_new_memoryset")
        """
        memories = self.to_list()
        destination = self._get_reset_destination_memoryset(destination, embedding_model)
        destination.insert(memories)
        return destination

    def clone(self, destination: LabeledMemoryset | str) -> LabeledMemoryset:
        """
        Clone the current memoryset into a new memoryset.

        Note:
            This will reset the destination memoryset if it already exists.

        Args:
            destination: The destination memoryset to clone this memoryset into, this can either be
                a memoryset instance, or the URL to a new memoryset, or the name of a table in the
                same database. A table for the destination will be created if it does not already
                exist.

        Returns:
            The destination memoryset that the memories were cloned into.

        Examples:
            Clone a local memoryset into a hosted database:
            >>> memoryset = LabeledMemoryset("file:./orca.db#my_memoryset")
            >>> memoryset.clone("https://<my-api-key>:<my-secret-key>@instance.orcadb.cloud/my-database#my_memoryset")

            Clone a local memoryset into a new table in the same database:
            >>> memoryset = LabeledMemoryset("file:./orca.db#my_memoryset")
            >>> memoryset.clone("my_new_memoryset")
        """
        memories = self.to_list()
        destination = self._get_reset_destination_memoryset(destination)
        if destination.url == self.url:
            logging.info("Warning: Source and destination are the same. No data will be cloned.")
            return self
        destination.insert(memories, compute_embeddings=self.embedding_model != destination.embedding_model)
        return destination

    def map(
        self,
        fn: Callable[[LabeledMemory], dict[str, Any] | LabeledMemory],
        destination: LabeledMemoryset | str | None = None,
    ) -> LabeledMemoryset:
        """
        Apply a function to all the memories in the memoryset and store them in the current
        memoryset or a new destination memoryset if it is provided.

        Note:
            If your function returns a column that already exists, then it overwrites it.

        Args:
            fn: Function that takes in the memory and returns a new memory or a dictionary
                containing the values to update in the memory.
            destination: The destination memoryset to store the results in, this can either be
                a memoryset instance, or the URL to a new memoryset, or the name of a table in the
                same database. A table for the destination will be created if it does not already
                exist.

        Returns:
            The destination memoryset with the updated memories.

        Examples:
            Add new metadata to all memories in the memoryset:
            >>> memoryset = LabeledMemoryset("file:./orca.db#my_memoryset")
            >>> memoryset.map(lambda m: dict(metadata=dict(**m.metadata, new_key="new_value")))

            Create a new memoryset with swapped labels in a new table in the same database:
            >>> memoryset = LabeledMemoryset("file:./orca.db#my_memoryset")
            >>> swapped_memoryset = memoryset.map(
            ...     lambda m: dict(label=1 if m.label == 0 else 0),
            ...     "my_swapped_memoryset"
            ... )
        """
        memories = self.to_list()
        destination = self._get_reset_destination_memoryset(destination)

        compute_embeddings = self.embedding_model != destination.embedding_model if destination else True

        def replace_fn(memory: LabeledMemory) -> LabeledMemory:
            result = fn(memory)
            # recompute embedding if the value has changed and the embedding was not provided
            if not compute_embeddings and memory.value != result["value"] and "embedding" not in result:
                result["embedding"] = destination.embedding_model.embed(result["value"])
            return result if isinstance(result, LabeledMemory) else replace(memory, **result)

        mapped_memories = [replace_fn(memory) for memory in memories]
        destination.insert(mapped_memories, compute_embeddings=compute_embeddings)
        return destination

    def filter(
        self, fn: Callable[[LabeledMemory], bool], destination: LabeledMemoryset | str | None = None
    ) -> LabeledMemoryset:
        """
        Filters the current memoryset using the given function and stores the result in the current
        memoryset or a new destination memoryset if it is provided.

        Note:
            This will reset the destination memoryset if it already exists.

        Args:
            fn: Function that takes in the memory and returns a boolean indicating whether the
                memory should be included or not.
            destination: The destination memoryset to store the results in, this can either be
                a memoryset instance, or the URL to a new memoryset, or the name of a table in the
                same database. A table for the destination will be created if it does not already
                exist.

        Returns:
            The destination memoryset with the filtered memories.

        Examples:
            Filter out memories with a label of 0:
            >>> memoryset = LabeledMemoryset("file:./orca.db#my_memoryset")
            >>> memoryset.filter(lambda m: m.label != 0)

            Create a new memoryset with some metadata in a new table in the same database:
            >>> memoryset = LabeledMemoryset("file:./orca.db#my_memoryset")
            >>> filtered_memoryset = memoryset.filter(
            ...     lambda m: m.metadata["key"] == "filter_value",
            ...     "my_filtered_memoryset"
            ... )
        """
        filtered_memories = [memory for memory in self.to_list() if fn(memory)]
        destination = self._get_reset_destination_memoryset(destination)
        destination.insert(filtered_memories, compute_embeddings=self.embedding_model != destination.embedding_model)
        return destination

    def finetune_reranker(
        self,
        data: DatasetLike,
        save_dir: str,
        training_args: RerankerTrainingArguments = RerankerTrainingArguments(),
        num_memories: int = 9,  # TODO: unify this default with the rac memory_lookup_count
    ) -> None:
        if self.reranker is None:
            self.reranker = SharedEncoderReranker("Alibaba-NLP/gte-base-en-v1.5")
        pairs_dataset = MemoryPairsDataset(
            samples=cast(list[tuple[str, int]], format_dataset(data)),
            lookup_fn=lambda query, num_memories: [
                (cast(str, memory.value), memory.label)
                for memory in self.lookup(query, k=num_memories, column_oriented=False)[0]
            ],
            num_memories=num_memories * self.reranker.compression,
        )
        self.reranker.finetune(save_dir, pairs_dataset, training_args)
        # TODO: save reranker embeddings to database

    def finetune_embedding_model(
        self,
        save_dir: str,
        destination: LabeledMemoryset | str | None = None,
        training_args: EmbeddingTrainingArguments = EmbeddingTrainingArguments(),
        train_data: DatasetLike | None = None,
        eval_data: DatasetLike | None = None,
    ):
        """
        Finetunes the embedding model for the memoryset.

        Note:
            This will reset the destination memoryset if it already exists.

        Args:
            save_dir: The directory to save the finetuned model to.
            destination: The destination memoryset to store the results in, this can either be
                a memoryset instance, or the URL to a new memoryset, or the name of a table in the
                same database. A table for the destination will be created if it does not already
                exist. If this is `None` the current memoryset will be used.
            training_args: The training arguments to use for the finetuning.
            train_data: The data to finetune on, if this is `None` the memories from the current
                memoryset will be used.
            eval_data: The data to evaluate the finetuned model on, if this is `None` a 10% holdout
                from the training data will be used.

        Returns:
            The destination memoryset with the finetuned embedding model. All memories will be
            re-embedded using the finetuned model.
        """
        memories = self.to_list()
        if train_data is not None:
            transformed_data = transform_data_to_dict_list(train_data)
            train_dataset = Dataset.from_dict(
                {
                    "value": [cast(InputType, m["text"] or m["image"]) for m in transformed_data],
                    "label": [m["label"] for m in transformed_data],
                }
            )
        else:
            train_dataset = self.to_dataset().select_columns(["value", "label"])
        if train_dataset.features["value"].dtype != "string":
            raise ValueError("fine tuning is only supported for text memories")

        if eval_data is not None:
            transformed_eval_data = transform_data_to_dict_list(eval_data)
            eval_dataset = Dataset.from_dict(
                {
                    "value": [cast(InputType, m["text"] or m["image"]) for m in transformed_eval_data],
                    "label": [m["label"] for m in transformed_eval_data],
                }
            )
        else:
            split_dataset = train_dataset.train_test_split(test_size=0.1)
            train_dataset = split_dataset["train"]
            eval_dataset = split_dataset["test"]

        finetuned_embedding_model = self.embedding_model.finetune_for_classification(
            save_dir,
            train_dataset,
            eval_dataset,
            training_args=training_args,
        )
        destination = self._get_reset_destination_memoryset(destination, finetuned_embedding_model)
        destination.insert(memories)
        return destination

    def drop_table(self, table_name: str | None = None):
        """
        Drop the table associated with this Memoryset.
        """
        if self.mode == "local" and isinstance(self.db, lancedb.DBConnection):
            try:
                self.db.drop_table(table_name or self.table_name)
            except FileNotFoundError:
                pass
            try:
                self.db.drop_table(f"rac_meta_{table_name or self.table_name}")
            except FileNotFoundError:
                pass
        elif self.mode == "hosted" and isinstance(self.db, OrcaDatabase):
            self.db.drop_table(table_name or self.table_name, error_if_not_exists=False)
            self.db.drop_table(f"rac_meta_{table_name or self.table_name}", error_if_not_exists=False)
            self.table = None
        else:
            raise Exception("Memoryset not initialized correctly")

    def reset(self):
        """
        Drop all data from the table associated with this Memoryset.
        """
        self.cache.clear()
        self.drop_table()
        if self.mode == "local":
            self._init_local_db()
        elif self.mode == "hosted":
            self._init_hosted_db()
        else:
            raise Exception("Memoryset not initialized correctly")

    def _drop_database(self, *, yes_i_am_sure: bool = False):
        """
        Drop the whole database that the table associated with this Memoryset lives in.
        """
        if not yes_i_am_sure:
            logging.warning("This will delete all data in the database. If you are sure, set `yes_i_am_sure` to True.")
        if self.mode == "local" and isinstance(self.db, lancedb.DBConnection):
            self.db.drop_database()
        elif self.mode == "hosted" and isinstance(self.db, OrcaDatabase):
            self.db.drop()
        else:
            raise Exception("Memoryset not initialized correctly")

    def analyze(self, log: bool = True) -> LabeledMemorysetAnalysisResults:
        memoryset = self.to_list()
        return LabeledMemorysetAnalysisResults(memoryset, lambda q, k: self.lookup(q, k=k), log)
