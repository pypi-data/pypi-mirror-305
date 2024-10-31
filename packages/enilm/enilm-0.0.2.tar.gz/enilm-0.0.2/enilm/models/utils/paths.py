from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Iterable, Optional

import enilm.config


@dataclass
class Paths:
    model: Path
    hist_path: Path
    hist_path_csv: Path
    train_duration_path: Path
    hist_test_path: Path
    hist_test_path_csv: Path
    checkpoint_model: Path


def get_paths(model_path_base: Path) -> Paths:
    return Paths(
        model=model_path_base / f"model.h5",
        hist_path=model_path_base / "train.hist.pkl",
        hist_path_csv=model_path_base / "train.hist.csv",
        train_duration_path=model_path_base / "train_duration.txt",
        hist_test_path=model_path_base / "test.hist.pkl",
        hist_test_path_csv=model_path_base / "test.hist.csv",
        checkpoint_model=model_path_base / "checkpoint.h5",
    )


class Captures(Enum):
    Epochs = "ep"
    SamplePeriod = "sp"


def create_model_path_base(
    config: enilm.config.ExpConfig,
    captures: Optional[Iterable[Captures]] = None,
) -> Path:
    """
    Captures are processed in order to generate subpaths
    """
    assert not config.model_id is None
    assert not config.exp_n is None

    # default subpaths based on captures
    if not captures:
        captures = [Captures.Epochs, Captures.SamplePeriod]

    path = Path("")
    for capture in captures:
        if capture == Captures.Epochs:
            assert not config.epochs is None
            path /= f"{capture.value}{config.epochs}"
        elif capture == Captures.SamplePeriod:
            assert not config.sample_period is None
            path /= f"{capture.value}{config.sample_period}"
    path /= f"{config.exp_num}_{config.model_id}"
    return path
