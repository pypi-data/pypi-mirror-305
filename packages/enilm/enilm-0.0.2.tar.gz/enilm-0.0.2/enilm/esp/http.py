from dataclasses import dataclass
from typing import Optional

import requests


class ConnFailedException(Exception):
    pass


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


def set_input_buffer(data: bytes) -> bool:
    assert params is not None
    assert isinstance(data, bytes)
    assert len(data) == params.input_n_bytes

    for _ in range(params.retries):
        resp = requests.put(params.esp_url + 'set_inbuf', data)
        if resp.status_code == 200 and resp.ok and resp.text == 'Ok!':
            return True

    return False


def get_inference_result(data: Optional[bytes] = None) -> bytes:
    assert params is not None

    if data is not None:
        set_input_buffer(data)

    res: bytes = b''
    for _ in range(params.retries):
        resp = requests.get(params.esp_url + 'infer')
        if resp.status_code == 200 and resp.ok:
            res = resp.content
            break
    if res == b'':
        raise ConnFailedException
    assert len(res) == params.output_n_bytes

    # res: np.ndarray = np.frombuffer(res, dtype=np.float32, count=params.n_outputs)
    return res
