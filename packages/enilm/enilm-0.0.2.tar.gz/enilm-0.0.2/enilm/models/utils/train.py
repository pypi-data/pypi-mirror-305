"""
Train and test a model with standard saving location
"""

from pathlib import Path
import dataclasses
import time
import pickle
from typing import Dict, Optional

import tensorflow as tf
import pandas as pd
import numpy as np

import enilm
from .paths import get_paths


@dataclasses.dataclass()
class TrainTestParams:
    model: tf.keras.Model
    x_chunks: np.ndarray
    y_chunks: np.ndarray
    test_x_chunks: np.ndarray
    test_y_chunks: np.ndarray
    epochs: int
    batch_size: int
    validation_split: float
    fit_params: Dict = dataclasses.field(default_factory=lambda: {})
    save_checkpoint: bool = False


@dataclasses.dataclass
class TrainTestResult:
    model: tf.keras.Model
    checkpoint_model: Optional[tf.keras.Model]
    train_hist: pd.DataFrame
    test_hist: pd.DataFrame
    train_duration: float


def train_test(model_path_base: Path, params: TrainTestParams) -> TrainTestResult:
    model_exists = model_path_base.exists()
    if model_exists:
        raise ValueError(
            "Path already exists. This function is intended to save new model in given path. Please chosse unexisting path"
        )
    model_path_base.mkdir()
    paths = get_paths(model_path_base)

    ### Train
    callbacks = []
    if params.save_checkpoint:
        callbacks.append(
            # https://keras.io/api/callbacks/model_checkpoint/
            tf.keras.callbacks.ModelCheckpoint(
                filepath=paths.checkpoint_model,
                save_weights_only=False,
                monitor="val_denorm_mae",
                mode="min",
                save_best_only=True,
                save_freq="epoch",
            )
        )

    start = time.perf_counter()
    train_hist = pd.DataFrame(
        params.model.fit(
            x=params.x_chunks,
            y=params.y_chunks,
            epochs=params.epochs,
            batch_size=params.batch_size,
            validation_split=params.validation_split,
            callbacks=callbacks,
            **params.fit_params,
        ).history,
    )
    train_duration: float = time.perf_counter() - start

    enilm.models.utils.file.save_model(params.model, paths.model)
    with open(paths.hist_path, "wb") as fp:
        pickle.dump(train_hist, fp)
    train_hist.to_csv(paths.hist_path_csv)
    with open(paths.train_duration_path, "w") as fp:
        fp.write(str(train_duration))

    ### Test
    test_hist = pd.DataFrame(
        [
            params.model.evaluate(
                x=params.test_x_chunks,
                y=params.test_y_chunks,
                batch_size=params.batch_size,
            )
        ],
        columns=params.model.metrics_names,
    )

    with open(paths.hist_test_path, "wb") as fp:
        pickle.dump(test_hist, fp)
    test_hist.to_csv(paths.hist_test_path_csv)

    checkpoint_model = None
    if params.save_checkpoint:
        checkpoint_model = enilm.models.utils.file.load_model_with_denorm_mae(
            paths.checkpoint_model
        )

    return TrainTestResult(
        model=params.model,
        checkpoint_model=checkpoint_model,
        train_hist=train_hist,
        test_hist=test_hist,
        train_duration=train_duration,
    )


def load(model_path_base: Path) -> TrainTestResult:
    assert model_path_base.exists()
    paths = get_paths(model_path_base)

    ### From training
    model = enilm.models.utils.file.load_model(
        paths.model, custom_objects={"DenormMAE": enilm.keras.metrics.DenormMAE}
    )
    checkpoint_model = enilm.models.utils.file.load_model_with_denorm_mae(
        paths.checkpoint_model
    )
    with open(paths.hist_path, "rb") as fp:
        train_hist = pickle.load(fp)
    with open(paths.train_duration_path, "r") as fp:
        train_duration = float(fp.read())

    ### From testing
    with open(paths.hist_test_path, "rb") as fp:
        test_hist = pickle.load(fp)

    return TrainTestResult(
        model=model,
        checkpoint_model=checkpoint_model,
        train_hist=train_hist,
        test_hist=test_hist,
        train_duration=train_duration,
    )
