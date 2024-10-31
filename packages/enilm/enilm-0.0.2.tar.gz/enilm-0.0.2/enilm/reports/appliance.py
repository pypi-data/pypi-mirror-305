from typing import Union, Iterable

import pandas as pd
import nilmtk
from nilmtk import Appliance

from enilm.etypes import AppName, DatasetID
from enilm.datasets import get_nilmtk_dataset
from enilm.appliances import get_elec


def check_app_in_ds(
    apps: Iterable[Union[Appliance, AppName]],
    ds_id: DatasetID,
) -> pd.DataFrame:
    nilmtk_ds: nilmtk.dataset.DataSet = get_nilmtk_dataset(ds_id)
    data = []
    for elec in nilmtk_ds.elecs():
        building: int = elec.building()
        row = [building]
        for app in apps:
            try:
                get_elec(app, elec)
                row.append(True)
            except:
                row.append(False)
        data.append(row)

    columns = ["building"] + list(map(str, apps))
    return pd.DataFrame(data, columns=columns)
