"""Helper methods for nilmtk appliances"""
from typing import Union, Iterable, List

import numpy as np
import nilmtk
from nilmtk import Appliance, MeterGroup, ElecMeter
from nilmtk.electric import Electric

import enilm.etypes


def get_appliance_by_label_name_from_nilmtk_metergroup(label_name: str, elec: MeterGroup) -> Appliance:
    """
    name is assumed to be generated using `nilmtk.Appliance.label`
    """
    apps_found_in_elec_with_this_name: List[Appliance] = []
    for app in elec.appliances:
        if app.label(True).lower() == label_name.lower():
            apps_found_in_elec_with_this_name.append(app)
        elif app.label(False).lower() == label_name.lower():
            apps_found_in_elec_with_this_name.append(app)

    if len(apps_found_in_elec_with_this_name) == 0:
        raise ValueError(f"App {label_name} not found")
    if len(apps_found_in_elec_with_this_name) > 1:
        raise ValueError(f"Found multiple apps with the same name {label_name}")
    return apps_found_in_elec_with_this_name[0]


def get_appliance(appliance_elec: Electric) -> Appliance:
    """
    Returns appliance of provided meter, if none or more than one appliance are attached to the meter an error is raised
    The type can be used to retrieve the appliance from the meter group and uniquely identify it (see `get_elec`)

    Parameters
    ----------
    appliance_elec electricity meter of the appliance (either ElecMeter or MeterGroup)

    Returns
    -------
    appliance id
    """
    assert hasattr(appliance_elec, "appliances")
    if not len(appliance_elec.appliances) == 1:
        raise ValueError("An ElecMeter with exactly one appliance is expected")
    return appliance_elec.appliances[0]


def get_elec(app: Union[Appliance, str], elec: MeterGroup) -> Union[ElecMeter, MeterGroup]:
    """
    Returns meter (either one meter as `ElecMeter` or multiple meters as a `MeterGroup`) of the corresponding appliance
    from the provided meter group `elec`
    """
    assert isinstance(elec, MeterGroup)
    try:
        if isinstance(app, str):
            return elec[app]
        elif isinstance(app, Appliance):
            return elec[app.identifier.type, app.identifier.instance]
        else:
            raise ValueError("App is expected to be either a string (that uniquley identify the required appliance) or an instance " "of `nilmtk.appliance.Appliance`")
    except Exception as e:
        if isinstance(app, str):
            # get `Appliance` from string
            some_app: Appliance
            for some_app in elec.appliances:
                if some_app.type["type"] == app:
                    app = some_app
                    break
            else:
                raise ValueError(f"Cannot find provided app {app} in elec meter")

        if e.args[0].startswith("search terms match"):
            # in REFIT both fridge,1 and freezer,1 are classified as of type fridge and thus calling `elec['freezer', 1]`
            # would generate an Exception with the following message: "search terms match 2 appliances"
            # WARN this is only a workaround and not tested thoroughly!
            for meter in elec.meters:
                if len(meter.appliances) == 1 and meter.appliances[0] == app:
                    return meter
        raise e


def to_str(apps_names: Iterable[Union[nilmtk.Appliance, enilm.etypes.AppName]]) -> List[enilm.etypes.AppName]:
    res = []
    for app in apps_names:
        if isinstance(app, nilmtk.Appliance):
            res.append(to_label(app))
        else:
            assert isinstance(app, enilm.etypes.AppName)
            res.append(app)
    return res


def to_label(app: nilmtk.Appliance):
    return app.label(True).lower()


def from_label(label: str):
    """
    where label is generated using nilmtk.Appliance.label(True)
    """
    raise NotImplementedError


def activations(app_data_np: np.ndarray):
    """see `nilmtk.electric.get_activations`"""
    on_power_threshold = app_data_np.mean()
    when_on = app_data_np > on_power_threshold
    state_changes = np.diff(when_on.astype(np.int8))

    switch_on_events = np.where(state_changes == 1)[0]
    switch_off_events = np.where(state_changes == -1)[0]
    n_events = min([len(switch_on_events), len(switch_off_events)])

    activations = []
    border = 1
    for on, off in zip(switch_on_events[:n_events], switch_off_events[:n_events]):
        on -= 1 + border
        if on < 0:
            on = 0
        off += border
        activation = app_data_np[on:off]
        # throw away any activation with any NaN values
        if activation.size > 0:
            activations.append(activation)

    return activations


def as_nilmtk(house_elec, apps_labels: List[str]) -> List[nilmtk.Appliance]:
    """Returns corresponding list of `nilmtk.appliance.Appliance`"""
    return [
        enilm.appliances.get_appliance_by_label_name_from_nilmtk_metergroup(
            label_name=app_name,
            elec=house_elec,
        )
        for app_name in apps_labels
    ]


def as_elecs(house_elec, apps_nilmtk: List[nilmtk.appliance.Appliance]) -> List[nilmtk.ElecMeter]:
    """Returns correspondig list the electric meter (`nilmtk.elecmeter.ElecMeter`) for each appliance"""
    res = []
    for app_nilmtk in apps_nilmtk:
        assert isinstance(app_nilmtk, nilmtk.appliance.Appliance)
        res.append(enilm.appliances.get_elec(app=app_nilmtk, elec=house_elec))
    return res
