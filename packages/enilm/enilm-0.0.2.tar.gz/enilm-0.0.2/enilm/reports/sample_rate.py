from typing import Union, Iterable
from dataclasses import dataclass

from nilmtk import ElecMeter, MeterGroup
from nilmtk.electric import Electric

from enilm.appliances import get_appliance


@dataclass
class SampleRateInfo:
    app: str = ''
    sample_period:int = 0 # sec
    sample_rate:float = 0.0 # Hz
    n_samples_per_day:int = 0

def get_info(elec: ElecMeter) -> SampleRateInfo:
    info = SampleRateInfo()

    if isinstance(elec, MeterGroup) or elec.is_site_meter():
        # mains
        info.app = 'mains'
    elif isinstance(elec, ElecMeter):
        # appliance
        info.app = get_appliance(elec).label(True)
    else:
        raise ValueError(f'Unexpected type of ElecMeter: {type(elec)}')

    info.sample_period = elec.sample_period()
    info.sample_rate = 1 / elec.sample_period()
    info.n_samples_per_day = round((1 / elec.sample_period()) * 60 * 60 * 24)

    return info

def sample_rate_info(elecs: Union[Iterable[ElecMeter], ElecMeter]) -> str:
    """
    Sample output for mains, kettle and washing machine from REFIT building 3:
    ```
    Mains:
        Sample Period: 7
        Sample Rate: 0.14Hz
        Number of samples/day: 12,343
    Washer dryer:
        Sample Period: 7
        Sample Rate: 0.14Hz
        Number of samples/day: 12,343
    Washer dryer:
        Sample Period: 7
        Sample Rate: 0.14Hz
        Number of samples/day: 12,343
    ```


    :param elecs: elecs to report about
    :return: string of all elecs sample period, rate and number of samples per day
    """
    if isinstance(elecs, Electric):
        elecs = [elecs]

    results = ''
    for elec in elecs:
        info = get_info(elec)
        results += f'{info.app.capitalize()}:'
        results += f'\n\tSample Period: {info.sample_period} seconds'
        results += f'\n\tSample Rate: {info.sample_rate:.2}Hz'
        results += f'\n\tNumber of samples/day: {info.n_samples_per_day:,}'
        results += '\n'

    return results.strip()


if __name__ == '__main__':
    test_sample_rate_info = False
    if test_sample_rate_info:
        from enilm.loaders import load_refit

        loaded = load_refit(building_nr=1)
        print(sample_rate_info(loaded.elec))
        # print(sample_rate_info([
        #     loaded.elec,
        #     get_elec('washer dryer', loaded.elec),
        # ]))
