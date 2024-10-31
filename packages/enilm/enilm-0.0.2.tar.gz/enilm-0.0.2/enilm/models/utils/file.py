from pathlib import Path

import tensorflow as tf
from enilm import convert
from enilm.constants import MemUnit


def save_model(model: tf.keras.Model, path: Path):
    model.save(path, save_format='h5')


def load_model(path: Path, **kwargs) -> tf.keras.Model:
    return tf.keras.models.load_model(path, **kwargs)


def load_model_with_denorm_mae(path: Path, **kwargs) -> tf.keras.Model:
    from enilm.keras.metrics import DenormMAE

    kwargs['custom_objects'] = {
        'DenormMAE': DenormMAE
    }

    return load_model(path, **kwargs)


def get_file_size(path: Path, unit: MemUnit = MemUnit.MiB) -> float:
    size_bytes = path.stat().st_size
    return convert.size(size_bytes, MemUnit.B, unit)
