import io
import json
from collections.abc import Mapping
from typing import Any, Literal, TypedDict, cast

import numpy as np
import pandas as pd
from datasets import Dataset
from PIL import Image
from torch.utils.data import DataLoader as TorchDataLoader
from torch.utils.data import Dataset as TorchDataset

from orcalib import ColumnName

from .memory_types import DatasetLike, InputType, LabeledMemory, LabeledMemoryLookup


def pil_image_to_bytes(image: Image.Image, format: str = "JPEG") -> bytes:
    byte_array = io.BytesIO()
    if format == "JPEG":
        image = image.convert("RGB")
    image.save(byte_array, format=format)
    byte_data = byte_array.getvalue()
    return byte_data


# Convert Bytes to PIL Image
def bytes_to_pil_image(byte_data: bytes) -> Image.Image:
    byte_array = io.BytesIO(byte_data)
    image = Image.open(byte_array)
    return image


class MemoryToInsert(TypedDict):
    text: str | None
    image: bytes | Image.Image | None
    label: int
    label_name: str | None
    metadata: str | None
    memory_version: int
    embedding: list[float] | None


def _transform_to_memory_to_insert_dict(
    item: LabeledMemory | Mapping | tuple, mode: Literal["hosted", "local"] = "local"
) -> MemoryToInsert:
    match item:
        case LabeledMemory():
            memory_to_insert: MemoryToInsert = {
                "text": item.value if isinstance(item.value, str) else None,
                "image": (
                    pil_image_to_bytes(item.value)
                    if mode == "local" and isinstance(item.value, Image.Image)
                    else item.value
                    if isinstance(item.value, Image.Image)
                    else None
                ),
                "label": item.label,
                "label_name": item.label_name,
                "metadata": json.dumps(item.metadata) if item.metadata else None,
                "memory_version": 1,
                "embedding": item.embedding.tolist() if item.embedding is not None else None,
            }
            return memory_to_insert
        # This also handles the dict case
        case Mapping():
            label = item["label"]
            if label is None:
                raise ValueError("Label must be provided.")
            label_name = item.get("label_name", None)
            metadata = item.get("metadata", None)
            embedding = item.get("embedding", None)
            if "value" in item:
                value = item["value"]
            elif "text" in item:
                value = item["text"]
            elif "image" in item:
                value = item["image"]
            else:
                keys = [k for k in item.keys() if k != "label" and k != "label_name" and k != "metadata"]
                if len(keys) == 1:
                    value = item[keys[0]]
                else:
                    raise ValueError("No 'value' column found and one could not be inferred.")

            ## Validate dictionary values ##

            # if value is bytes, transform to image before validation
            value = bytes_to_pil_image(value) if isinstance(value, bytes) else value

            # value validation
            if not isinstance(value, InputType):
                raise ValueError("value must be a string or PIL Image.")

            # Label validation
            if not isinstance(label, int):
                raise ValueError("Label must be an int.")

            # Label name validation
            if label_name is not None and not isinstance(label_name, str):
                raise ValueError("Label name must be a string.")

            # Metadata validation
            if metadata is not None:
                if not isinstance(metadata, (str, dict)):
                    raise ValueError("Metadata must be a JSON-serializable string or dict.")
                if isinstance(metadata, str):
                    try:
                        metadata = json.loads(metadata)
                    except json.JSONDecodeError:
                        raise ValueError("Metadata must be a JSON-serializable string or dict.")

            if embedding is not None and (not isinstance(embedding, np.ndarray) or len(embedding.shape) != 1):
                raise ValueError("Embedding must be a 1D numpy array.")

            memory_to_insert: MemoryToInsert = {
                "text": value if isinstance(value, str) else None,
                "image": (
                    pil_image_to_bytes(value)
                    if mode == "local" and isinstance(value, Image.Image)
                    else value
                    if isinstance(value, Image.Image)
                    else None
                ),
                "label": label,
                "label_name": label_name,
                "metadata": json.dumps(metadata) if metadata else None,
                "memory_version": 1,
                "embedding": embedding.tolist() if embedding is not None else None,
            }
            return memory_to_insert

        case tuple():
            if len(item) == 2 and isinstance(item[0], InputType) and (isinstance(item[1], int)):
                memory_to_insert: MemoryToInsert = {
                    "text": item[0] if isinstance(item[0], str) else None,
                    "image": (
                        pil_image_to_bytes(item[0])
                        if mode == "local" and isinstance(item[0], Image.Image)
                        else item[0]
                        if isinstance(item[0], Image.Image)
                        else None
                    ),
                    "label": item[1],
                    "memory_version": 1,
                    "embedding": None,
                    "metadata": None,
                    "label_name": None,
                }
                return memory_to_insert
            else:
                raise ValueError(
                    "Tuple must only have two elements; the first being the data and the second being the label."
                )
        case _:
            raise ValueError(f"Item must be a LabeledMemory, a Mapping, or a tuple: {type(item)}")


def transform_data_to_dict_list(data: DatasetLike, mode: Literal["hosted", "local"] = "local") -> list[MemoryToInsert]:
    match data:
        case LabeledMemory():
            return [_transform_to_memory_to_insert_dict(data, mode)]
        case dict():
            return [_transform_to_memory_to_insert_dict(data, mode)]
        case list():
            return [_transform_to_memory_to_insert_dict(item, mode) for item in data]
        case pd.DataFrame():
            return [_transform_to_memory_to_insert_dict(item, mode) for item in data.to_dict("records")]
        case Dataset():
            return [_transform_to_memory_to_insert_dict(item, mode) for item in data]  # type: ignore -- For our purposes, we can assume the item type is a Mapping
        case TorchDataset():
            return [_transform_to_memory_to_insert_dict(item, mode) for item in data]
        case TorchDataLoader():
            return [_transform_to_memory_to_insert_dict(item[0], mode) for item in data]
        case _:
            raise ValueError(
                f"Dataset must be a list of tuples, dicts, or LabeledMemories, or a single DataFrame, HuggingFace Dataset, Torch Dataset, Torch Data Loader, LabeledMemory, or dict: {type(data)}"
            )


class MemoryLookupResults(TypedDict):
    """Column-oriented LabeledMemoryset lookup query results."""

    value: list[InputType]
    label: list[int]
    label_name: list[str | None]
    embedding: list[np.ndarray]
    metadata: list[dict[str, Any] | None]
    lookup_score: list[float]
    memory_id: list[int]
    memory_version: list[int]


def format_lookup_results(
    results: tuple[int, list], original_query: np.ndarray, column_oriented: bool | None = False
) -> MemoryLookupResults | list[LabeledMemoryLookup]:
    if column_oriented:
        formatted_results: MemoryLookupResults | list[LabeledMemoryLookup] = {
            "value": [],
            "embedding": [],
            "memory_id": [],
            "memory_version": [],
            "label": [],
            "label_name": [],
            "metadata": [],
            "lookup_score": [],
        }
    else:
        formatted_results: MemoryLookupResults | list[LabeledMemoryLookup] = []

    for row in results[1]:
        metadata = json.loads(row[0]) if row[0] is not None else {}
        if row[1] is not None:
            if isinstance(row[1], bytes):
                value = bytes_to_pil_image(row[1])
            else:
                value = row[1]
        else:
            value = row[2]

        if column_oriented:
            assert isinstance(formatted_results, dict)
            formatted_results["value"].append(value)
            formatted_results["embedding"].append(np.array(row[6]))
            formatted_results["memory_id"].append(row[7])
            formatted_results["memory_version"].append(row[5])
            formatted_results["label"].append(row[3])
            formatted_results["label_name"].append(row[4])
            formatted_results["metadata"].append(metadata)
            formatted_results["lookup_score"].append(np.dot(original_query, np.array(row[6])))
        else:
            assert isinstance(formatted_results, list)
            formatted_results.append(
                LabeledMemoryLookup(
                    value=value,
                    embedding=row[6],  # embedding
                    memory_id=row[7],  # row_id for the memory data accessed
                    memory_version=row[5],  # memory_version
                    label=row[3],  # label
                    label_name=row[4],  # label_name
                    metadata=metadata,
                    lookup_score=np.dot(original_query, np.array(row[6])),  # Calculate inner product
                )
            )
    return formatted_results


class MemoryRecord(TypedDict):
    id: str
    text: str | None
    image: bytes | None
    label: int
    label_name: str | None
    embedding: np.ndarray
    metadata: str


def transform_rows_to_labeled_memories(
    memory_records: list[dict[str, Any]] | list[tuple[int, dict[ColumnName, Any]]]
) -> list[LabeledMemory]:
    if len(memory_records) == 0:
        return []
    if isinstance(memory_records[0], tuple):
        memory_records = cast(list[tuple[int, dict[ColumnName, Any]]], memory_records)
        memory_records = [{"_rowid": memory_record[0], **memory_record[1]} for memory_record in memory_records]

    memoryset: list[LabeledMemory] = []
    for record in memory_records:
        memory_record = cast(MemoryRecord, record)
        label = memory_record.get("label", None)
        if label is None:
            raise ValueError("Label must be provided.")
        else:
            metadata = memory_record.get("metadata", None)
            embedding = memory_record.get("embedding")
            if isinstance(embedding, list):
                embedding = np.array(embedding)
            memoryset.append(
                LabeledMemory(
                    value=memory_record.get("value", memory_record.get("text", memory_record.get("image", None))),
                    label=label,
                    label_name=memory_record.get("label_name", None),
                    embedding=embedding,
                    metadata=json.loads(metadata) if metadata else {},
                    memory_version=memory_record.get("memory_version", 1),
                    memory_id=cast(int, memory_record.get("_rowid")),
                )
            )
    return memoryset
