from pathlib import Path

import numpy as np


def load(arr_path: Path):
    return np.load(arr_path)


def save(arr: np.ndarray, arr_path: Path, verbose=True):
    arr_path.parent.mkdir(parents=True, exist_ok=True)
    np.save(arr_path, arr)


def compute_or_load(fn, fn_params, arr_path: Path):
    if arr_path.exists():
        return load(arr_path)

    dict_result = fn(**fn_params)
    save(dict_result, arr_path)
    return dict_result
