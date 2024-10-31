from pathlib import Path
import json
from typing import Dict, Union, List, Optional

import numpy as np
import pandas as pd
import nilmtk

import enilm

Appliance = Union[nilmtk.Appliance, enilm.etypes.AppName]
Appliances = List[Appliance]


def save_xyarry(xy: enilm.etypes.xy.XYArray, folder: Path):
    assert folder.exists() and folder.is_dir()
    np.save(str(Path(folder, "x.npy")), xy.x)
    for an in xy.y.keys():
        np.save(str(Path(folder, f"y_{an}.npy")), xy.y[an])


def save_pd_timestamps_ndarray(path: Path, arr: enilm.etypes.arr.PDTimestamps):
    assert isinstance(arr[0], pd.Timestamp)
    np.save(
        path,
        enilm.convert.pd_timestamps_to_np(arr),
    )


def save_times_xyarry(xy: enilm.etypes.xy.XYNPTimesArray, folder: Path):
    assert folder.exists() and folder.is_dir()
    assert isinstance(xy.x[0], pd.Timestamp)
    save_pd_timestamps_ndarray(str(Path(folder, "x.npy")), xy.x)
    for an in xy.y.keys():
        save_pd_timestamps_ndarray(str(Path(folder, f"y_{an}.npy")), xy.y[an])


def load_xyarry(folder: Path) -> enilm.etypes.xy.XYArray:
    assert folder.exists() and folder.is_dir()
    x = np.load(str(Path(folder, "x.npy")))
    y = {}
    for app_arr_file in folder.glob("y_*.npy"):
        an = app_arr_file.name[2:-4]
        y[an] = np.load(str(app_arr_file))
    return enilm.etypes.xy.XYArray(x, y)


def load_times_xyarray(folder: Path) -> enilm.etypes.xy.XYNPTimesArray:
    return load_xyarry(folder)


def save_all_info(
    xy: enilm.etypes.xy.XYArray,
    appliances: Appliances,
    win_size: int,
    parent: Path,
    xy_times: Optional[enilm.etypes.xy.TimesTrainTestPDXYArray] = None,
):
    assert not parent.exists()
    parent.mkdir(parents=True)

    # data in xy folder
    path_xy = parent / "xy"
    path_xy.mkdir()
    save_xyarry(xy, path_xy)

    # times in times folder
    if xy_times:
        path_times = parent / "times"
        path_times.mkdir()
        save_times_xyarry(xy_times, path_times)

    # normalized in norm folder
    norm_params: enilm.etypes.xy.XYNormParams = enilm.xy.norm.compute_mean_std(
        xy.x, xy.y
    )
    path_norm = parent / "norm"
    path_norm.mkdir()
    with open(path_norm / "norm_params.json", "w", encoding="utf=8") as f:
        json.dump(norm_params._asdict(), f)
    x_norm: np.ndarray
    y_norm: Dict[enilm.etypes.AppName, np.ndarray]
    x_norm, y_norm = enilm.xy.norm.norm(
        xy,
        appliances,
        x_mean=norm_params.x_mean,
        x_std=norm_params.x_std,
        y_mean=norm_params.y_mean,
        y_std=norm_params.y_std,
    )
    enilm.xy.cache.save_xyarry(enilm.etypes.xy.XYArray(x_norm, y_norm), path_norm)

    # chunks in chunks folder
    x_chunks: np.ndarray
    y_chunks: Dict[enilm.etypes.AppName, np.ndarray]
    x_chunks = enilm.windowing.rolling(x_norm, win_size)
    y_chunks = {
        k.replace(" ", "_"): enilm.windowing.midpoints(v, win_size)
        for k, v in y_norm.items()
    }
    path_chunks = parent / "chunks"
    path_chunks.mkdir()
    enilm.xy.cache.save_xyarry(enilm.etypes.xy.XYArray(x_chunks, y_chunks), path_chunks)
