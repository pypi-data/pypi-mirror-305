from dataclasses import dataclass
from typing import Optional


@dataclass
class Params:
    input_n_bytes: int
    output_n_bytes: int
    esp_url: str
    retries: int = 2


params: Optional[Params] = None


def set_params(new_params: Params):
    global params
    assert new_params.esp_url.endswith('/')
    params = new_params
