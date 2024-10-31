from typing import Dict, Literal, Tuple, Optional, Iterable, Union

import nilmtk
import numpy as np
import pandas as pd


import enilm

def _load(_set: Literal['train', 'test'],
          config: enilm.config.ExpConfig,
          get_temporal_data: bool = False, ) \
        -> Union[
            Tuple[
                enilm.etypes.arr.SamplesF64, 
                Dict[enilm.etypes.AppName, enilm.etypes.arr.SamplesF64]
            ],
            Tuple[
                enilm.etypes.arr.SamplesF64, 
                Dict[enilm.etypes.AppName, enilm.etypes.arr.SamplesF64], 
                enilm.etypes.arr.PDTimestamps, 
                Dict[enilm.etypes.AppName, enilm.etypes.arr.PDTimestamps]],
        ]:
    selected_data_sel: Iterable[enilm.config.DataSel]
    if _set == 'train':
        selected_data_sel = config.train
    elif _set == 'test':
        selected_data_sel = config.test
    else:
        raise ValueError

    # declare results
    x: np.ndarray = np.array([])
    y: Dict[enilm.etypes.AppName, np.ndarray] = {}
    x_times: np.ndarray = np.array([])
    y_times: Dict[enilm.etypes.AppName, np.ndarray] = {}

    for data_sel in selected_data_sel:
        # repeated variables depending on set
        dataset: enilm.etypes.Datasets = data_sel.dataset
        houses: Iterable[enilm.etypes.HouseNr] = data_sel.houses
        sections: Optional[Dict[enilm.etypes.HouseNr, Iterable[nilmtk.TimeFrame]]] = data_sel.sections

        # load data for each house
        for house in houses:
            # create load kwargs
            load_kwargs = enilm.load_kwargs.LoadKwargs()
            if config.sample_period is not None:
                load_kwargs.sample_period = config.sample_period
            if sections is not None:
                load_kwargs.sections = sections[house]

            # load elecs
            mains: nilmtk.ElecMeter
            apps_elecs: Dict[enilm.etypes.AppName, nilmtk.ElecMeter]
            with enilm.context.sec(header=f'loading {_set} elecs for house {house}', mem=True):
                loaded = enilm.datasets.loaders.load(dataset, house)
                mains = loaded.elec.mains()
                apps_elecs = {}
                for app_name in config.appliances:
                    apps_elecs[app_name] = enilm.appliances.get_elec(app_name, loaded.elec)

            # load x for mains, y for each appliance
            with enilm.context.sec(header=f'loading & aligning data for house {house}', mem=True):
                x_ser: pd.Series
                y_ser: Dict[enilm.etypes.AppName, pd.Series]
                x_ser, y_ser = enilm.xy.get_and_align_multi_y(mains, apps_elecs, load_kwargs)

                x = np.concatenate([x, x_ser.to_numpy()])
                if get_temporal_data:
                    x_times = np.concatenate([x_times, x_ser.index.to_numpy()])

                if len(y) == 0:
                    # first appliance
                    y = {k: y_ser[k].to_numpy() for k in config.appliances}
                    if get_temporal_data:
                        y_times = {k: y_ser[k].index.to_numpy() for k in config.appliances}
                else:
                    y = {k: np.concatenate([y[k], y_ser[k].to_numpy()]) for k in config.appliances}
                    if get_temporal_data:
                        y_times = {k: np.concatenate([
                            y_times[k],
                            y_ser[k].index.to_numpy()
                        ]) for k in config.appliances}

    if config.shuffle:
        perm = np.random.permutation(len(x))
        x = x[perm]
        y = {k: v[perm] for k, v in y.items()}
        if get_temporal_data:
            x_times = x_times[perm]
            y_times = {k: v[perm] for k, v in y_times.items()}

    # sanity check
    for app_y in y.values():
        assert len(x) == len(app_y)

    # return
    if get_temporal_data:
        return x, y, x_times, y_times
    return x, y

def from_exp_config_with_times(
        config: enilm.config.ExpConfig,
    ) -> Tuple[
        enilm.etypes.xy.TrainTestXYArray, 
        enilm.etypes.xy.TimesTrainTestPDXYArray,
    ]:
    x_train, y_train, x_train_times, y_train_times = _load('train', config, get_temporal_data=True)
    x_test, y_test, x_test_times, y_test_times = _load('test', config, get_temporal_data=True)
    return (
        enilm.etypes.xy.TrainTestXYArray(
            train=enilm.etypes.xy.XYArray(x=x_train, y=y_train),
            test=enilm.etypes.xy.XYArray(x=x_test, y=y_test),
        ),
        enilm.etypes.xy.TimesTrainTestPDXYArray(
            train=enilm.etypes.xy.XYArray(x=x_train_times, y=y_train_times),
            test=enilm.etypes.xy.XYArray(x=x_test_times, y=y_test_times),
        ),
    )


def train_from_config(config: enilm.config.ExpConfig) -> enilm.etypes.xy.XYArray:
    x_train, y_train = _load('train', config)
    return enilm.etypes.xy.XYArray(x_train, y_train)


def test_from_config(config: enilm.config.ExpConfig) -> enilm.etypes.xy.XYArray:
    x_test, y_test = _load('test', config)
    return enilm.etypes.xy.XYArray(x_test, y_test)

def from_exp_config(config: enilm.config.ExpConfig) -> enilm.etypes.xy.TrainTestXYArray:
    return enilm.etypes.xy.TrainTestXYArray(
        train=train_from_config(config),
        test=test_from_config(config),
    )
