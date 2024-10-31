from pathlib import Path
from typing import Union, NamedTuple, Optional, List

import numpy as np
import pandas as pd
import yaml

from nilmtk import Appliance, ElecMeter, MeterGroup

import enilm.load_kwargs

class NormParams(NamedTuple):
    mean: float
    std: float

def normalize(x: Union[np.ndarray, pd.Series], mean_or_params: Optional[Union[NormParams, float]] = None, std: Optional[float] = None):
    if isinstance(mean_or_params, NormParams):
        mean = mean_or_params.mean
        std = mean_or_params.std
        return (x - mean) / std
    
    if mean_or_params is None:
        mean = np.mean(x)
        std = np.std(x)
        return (x - mean) / std
    
    if isinstance(mean_or_params, float):
        if std is None:
            raise ValueError("std must be provided if mean is provided")
        mean = mean_or_params
        return (x - mean) / std
    
    raise ValueError("mean must be either NormParams, float or None")


def denormalize(x: Union[np.ndarray, pd.Series], mean_or_params: Union[NormParams, float], std: Optional[float] = None):
    if isinstance(mean_or_params, NormParams):
        mean = mean_or_params.mean
        std = mean_or_params.std
        return (x * std) + mean
    elif isinstance(mean_or_params, float):
        if std is None:
            raise ValueError("std must be provided if mean is provided")
        mean = mean_or_params
        return (x * std) + mean
    
    raise ValueError("mean must be either NormParams or float")


def compute(x: Union[np.ndarray, pd.Series]) -> NormParams:
    return NormParams(float(np.mean(x)), float(np.std(x)))


class NoActivations(RuntimeError):
    pass


def compute_on_power_from_elec(
        elec: Union[ElecMeter, MeterGroup],
        on_power_threshold: Optional[int] = None,
        load_kwargs: Optional[enilm.load_kwargs.LoadKwargs] = None
) -> NormParams:
    """
    If `on_power_threshold` is not provided, then it is extracted from nilmtk see `nilmtk.appliance.on_power_threshold`
    """
    load_kwargs = load_kwargs.to_dict() if load_kwargs is not None else {}
    activations: List[pd.Series] = enilm.activations.get_appliance_activations(
        elec, on_power_threshold, **load_kwargs
    )
    if len(activations) == 0:
        raise NoActivations
    all_act: np.ndarray = np.concatenate(activations)
    return NormParams(float(np.mean(all_act)), float(np.std(all_act)))


def get_params(dataset: enilm.etypes.DatasetID, appliance: Union[Appliance, str] = None) -> NormParams:
    """
    if appliance is None, normalization params for mains is returned
    """
    config_file_path: Path = Path(__file__).parent.parent / "config.yaml"
    dataset_name = enilm.datasets.id_to_str(dataset)
    norm_params = yaml.safe_load(config_file_path.read_text())['norm']

    if dataset_name not in norm_params:
        raise ValueError

    app_name: str
    if appliance is None:
        app_name = 'mains'
    elif isinstance(appliance, Appliance):
        app_name = appliance.label()
    elif isinstance(appliance, str):
        app_name = appliance
    else:
        raise ValueError

    if app_name not in norm_params[dataset_name]:
        raise ValueError

    return NormParams(
        mean=norm_params[dataset_name][app_name]['mean'],
        std=norm_params[dataset_name][app_name]['std'],
    )
