from typing import Optional

import tensorflow as tf


class ConstantOutputLayer(tf.keras.layers.Layer):
    def __init__(self, constant: float = 0.0, **kwargs):
        super(ConstantOutputLayer, self).__init__(**kwargs)
        self.constant = constant

    def call(self, inputs):
        return tf.repeat(
            self.constant,
            tf.shape(inputs)[0]
        )

    def get_config(self):
        return {"constant": self.constant}


def constant(
    constant: float,
    win_size: int,
    with_reshape: bool = True,
    output_layer_name: Optional[str] = 'output',
) -> tf.keras.Model:
    model: tf.keras.Model = tf.keras.Sequential()
    if with_reshape:
        # add dummy dimension for each sample for the next Conv layer
        model.add(tf.keras.layers.Reshape((1, win_size, 1),
                                          input_shape=(win_size,), name='reshape'))
    model.add(tf.keras.layers.Input(shape=(1, win_size, 1), name='input'))
    model.add(ConstantOutputLayer(constant=constant, name=output_layer_name))
    return model

def zero(
    win_size: int,
    with_reshape: bool = True,
    output_layer_name: Optional[str] = 'output',
) -> tf.keras.Model:
    return constant(0.0, win_size, with_reshape, output_layer_name)
