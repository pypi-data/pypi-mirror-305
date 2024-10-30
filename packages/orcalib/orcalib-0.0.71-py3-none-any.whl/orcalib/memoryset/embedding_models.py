from __future__ import annotations

import logging
import os
from typing import cast

import numpy as np
import torch
from datasets import Dataset
from sentence_transformers import SentenceTransformer
from sklearn.metrics import f1_score
from tqdm.auto import trange
from transformers import (
    AutoConfig,
    AutoModelForSequenceClassification,
    CLIPConfig,
    EarlyStoppingCallback,
    PretrainedConfig,
    Trainer,
    TrainingArguments,
)

from ..torch_layers import SentenceEmbeddingGenerator
from .memory_types import InputType


class EmbeddingTrainingArguments(TrainingArguments):
    """Training arguments for finetuning an embedding model."""

    def __init__(
        self,
        output_dir: None = None,
        early_stopping_patience: int = 1,
        early_stopping_threshold: float | None = 0.005,
        eval_steps: int = 50,
        save_steps: int = 50,
        per_device_train_batch_size: int = 32,
        per_device_eval_batch_size: int = 32,
        gradient_accumulation_steps: int = 2,
        num_train_epochs: int = 2,
        logging_steps: int = 5,
        metric_for_best_model: str = "eval_f1_score",
        greater_is_better: bool = True,
        save_total_limit: int = 2,
        **kwargs,
    ):
        """
        Initialize training arguments for finetuning an embedding model.

        Note:
            This class extends HuggingFace's [`TrainingArguments`][transformers.TrainingArguments],
            with sensible defaults and additional arguments for finetuning embedding models.
            For documentation of all available arguments, see that class.

        Args:
            output_dir: Do not set this, pass it as the first argument to the finetune method instead.
            early_stopping_patience: stop after this many epochs of no improvement on the `metric_for_best_model`
            early_stopping_threshold: stop if the specified `metric_for_best_model` is not improving by at least this much
        """
        if output_dir is not None:
            raise ValueError(
                "output_dir of training_args must not be set. Pass it as the first argument to the finetune method instead."
            )
        if "eval_strategy" in kwargs:
            raise ValueError("eval_strategy cannot be overridden")
        if "save_strategy" in kwargs:
            raise ValueError("save_strategy cannot be overridden")
        if "load_best_model_at_end" in kwargs:
            raise ValueError("load_best_model_at_end cannot be overridden")
        if "remove_unused_columns" in kwargs:
            raise ValueError("remove_unused_columns cannot be overridden")
        super().__init__(
            output_dir="/dev/null",
            eval_steps=eval_steps,
            save_steps=save_steps,
            per_device_train_batch_size=per_device_train_batch_size,
            per_device_eval_batch_size=per_device_eval_batch_size,
            gradient_accumulation_steps=gradient_accumulation_steps,
            num_train_epochs=num_train_epochs,
            logging_steps=logging_steps,
            save_total_limit=save_total_limit,
            metric_for_best_model=metric_for_best_model,
            greater_is_better=greater_is_better,
            **kwargs,
            # these cannot be overridden
            eval_strategy="steps",
            save_strategy="steps",
            load_best_model_at_end=True,
            remove_unused_columns=False,
        )
        self.early_stopping_patience = early_stopping_patience
        self.early_stopping_threshold = early_stopping_threshold


class EmbeddingModelMeta(type):
    _default_models: dict[str, EmbeddingModel] = {}

    @property
    def CLIP_BASE(cls) -> EmbeddingModel:
        """CLIP-L14 embedding model"""
        if "clip_base" not in cls._default_models:
            cls._default_models["clip_base"] = EmbeddingModel("sentence-transformers/clip-ViT-L-14", 1, 768)
        return cls._default_models["clip_base"]

    @property
    def GTE_BASE(cls) -> EmbeddingModel:
        """Alibaba GTE-Base v1.5 embedding model"""
        if "gte_base" not in cls._default_models:
            cls._default_models["gte_base"] = EmbeddingModel("Alibaba-NLP/gte-base-en-v1.5", 1)
        return cls._default_models["gte_base"]


class EmbeddingModel(metaclass=EmbeddingModelMeta):
    """
    Embedding models for use with memorysets
    """

    model_whitelist = [
        "sentence-transformers/clip-ViT-L-14",
        "Alibaba-NLP/gte-base-en-v1.5",
        "Alibaba-NLP/gte-large-en-v1.5",
        "sentence-transformers/multi-qa-mpnet-base-dot-v1",
        "distilbert-base-uncased",
        "distilbert-base-cased",
        "bert-base-cased",
        "bert-base-uncased",
        "roberta-base",
        "roberta-large",
    ]

    def __init__(self, name: str, version: int = 0, embedding_dim: int | None = None, tokenizer: str | None = None):
        """
        Initialize an embedding model

        Warning:
            Only the models that are available as class properties like `EmbeddingModel.CLIP_BASE` as
            well as fine-tuned versions of them are guaranteed to work.

        Args:
            name: the name of the model to use, can be a HuggingFace model name or path to a local saved model,
                only models that are available as class properties like `EmbeddingModel.CLIP_BASE` as well as fine-tuned
                versions of them are guaranteed to work
            version: optional version number of the model to use, this is only used for default models
            embedding_dim: optional overwrite for embeddings dimension in case it is not correctly specified in the config
            tokenizer: optional name of a tokenizer model to use, if not given it will be the same as `name`
        """
        if name not in self.model_whitelist and not os.path.isdir(name):
            logging.warning(f"Model {name} is not in the whitelist, it may not work correctly")
        self.name = name
        self.tokenizer_name = tokenizer or name
        self.version = version
        self.config: PretrainedConfig = AutoConfig.from_pretrained(name, trust_remote_code=True)
        if embedding_dim is not None:
            self.embedding_dim = embedding_dim
        else:
            self.embedding_dim = getattr(self.config, "projection_dim", getattr(self.config, "hidden_size", None))
            if self.embedding_dim is None:
                raise ValueError(f"Could not determine embedding dimension from {self.config}")

    @property
    def embedder(self) -> SentenceTransformer | SentenceEmbeddingGenerator:
        if not hasattr(self, "_embedder"):
            if isinstance(self.config, CLIPConfig):
                self._embedder = SentenceTransformer(self.name, trust_remote_code=True)
            else:
                self._embedder = SentenceEmbeddingGenerator(
                    base_model=self.name, tokenizer_model=self.tokenizer_name, frozen=True, normalize=True
                )
        return self._embedder

    @property
    def max_sequence_length(self) -> int:
        if isinstance(self.embedder, SentenceTransformer):
            return self.embedder.max_seq_length
        else:
            return self.embedder.max_sequence_length

    @max_sequence_length.setter
    def max_sequence_length(self, value: int):
        if isinstance(self.embedder, SentenceTransformer):
            self.embedder.max_seq_length = value
        else:
            self.embedder.max_sequence_length = value

    def embed(
        self,
        data: InputType | list[InputType],
        show_progress_bar: bool = False,
        batch_size: int = 32,
    ) -> np.ndarray:
        """
        Generate embeddings for the given input

        Args:
            data: the data to encode, will be converted to a list if a scalar is given
            show_progress_bar: whether to show a progress bar
            batch_size: the size of the batches to use

        Returns:
            matrix with embeddings of shape `len_data` x `embedding_dim`
        """
        data = [data] if not isinstance(data, list) else data
        if len(data) == 0:
            return np.empty((0,))
        # generate embeddings
        if isinstance(self.embedder, SentenceTransformer):
            return self.embedder.encode(
                data,  # type: ignore -- types are wrong, image is accepted here
                show_progress_bar=show_progress_bar,
                normalize_embeddings=True,
                batch_size=batch_size,
            )
        else:
            if not isinstance(data[0], str):
                raise ValueError(f"{self.name} embedding model only supports strings")
            if len(data) <= batch_size:
                return self.embedder.encode(cast(list[str], data)).cpu().numpy()
            else:
                results = []
                for i in trange(
                    0,
                    len(data),
                    batch_size,
                    disable=not show_progress_bar,
                ):
                    batch = cast(list[str], data[i : i + batch_size])
                    results.append(self.embedder.encode(batch).cpu().numpy())
                return np.vstack(results)

    def finetune_for_classification(
        self,
        output_dir: str,
        train_dataset: Dataset,
        eval_dataset: Dataset,
        training_args: EmbeddingTrainingArguments,
    ) -> EmbeddingModel:
        """
        Finetune the embedding model for a classification task

        Args:
            values: text values to use for training
            labels: integer labels to use for training
            eval_values: text values to use for evaluation
            eval_labels: integer labels to use for evaluation
            training_args: training arguments to use, if not given a default will be used

        Returns:
            A new embedding model that is finetuned for the given classification task
        """
        training_args.output_dir = output_dir

        embedder = self.embedder
        assert isinstance(embedder, SentenceEmbeddingGenerator)

        num_labels = len(set(train_dataset["label"]))
        classification_model = AutoModelForSequenceClassification.from_pretrained(
            self.name,
            trust_remote_code=True,
            num_labels=num_labels,
        )
        max_sequence_length = embedder.get_max_sequence_length(cast(list[str], train_dataset["value"]))

        def collate_fn(batch: list[dict]):
            input_ids, attention_mask = embedder.tokenize(
                [b["value"] for b in batch], sequence_length=max_sequence_length, return_tensors=True
            )
            batch_labels = torch.tensor([b["label"] for b in batch])
            return dict(input_ids=input_ids, attention_mask=attention_mask, labels=batch_labels)

        def compute_metrics(eval_pred):
            logits, labels = eval_pred
            predictions = np.argmax(logits, axis=1)
            return {
                "accuracy": (predictions == labels).mean(),
                "f1_score": f1_score(labels, predictions, average="weighted" if num_labels > 2 else "binary"),
            }

        trainer = Trainer(
            model=classification_model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
            callbacks=[
                EarlyStoppingCallback(
                    early_stopping_patience=training_args.early_stopping_patience,
                    early_stopping_threshold=training_args.early_stopping_threshold,
                )
            ],
            data_collator=collate_fn,
            compute_metrics=compute_metrics,
        )
        trainer.train()
        trainer.save_model(training_args.output_dir)
        embedder.tokenizer.save_pretrained(training_args.output_dir)
        return EmbeddingModel(training_args.output_dir, embedding_dim=self.embedding_dim)
