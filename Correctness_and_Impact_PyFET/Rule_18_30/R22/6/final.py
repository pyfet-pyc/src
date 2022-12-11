# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/alpha_dropout.py
# Compiled at: 2022-08-11 21:20:35
# Size of source mod 2**32: 2329 bytes
"""Contains the AlphaDropout layer."""
import tensorflow.compat.v2 as tf
from keras import backend
from keras.engine import base_layer
from keras.utils import tf_utils
from tensorflow.python.util.tf_export import keras_export

@keras_export('keras.layers.AlphaDropout')
class AlphaDropout(base_layer.BaseRandomLayer):
    __doc__ = 'Applies Alpha Dropout to the input.\n\n    Alpha Dropout is a `Dropout` that keeps mean and variance of inputs\n    to their original values, in order to ensure the self-normalizing property\n    even after this dropout.\n    Alpha Dropout fits well to Scaled Exponential Linear Units\n    by randomly setting activations to the negative saturation value.\n\n    Args:\n      rate: float, drop probability (as with `Dropout`).\n        The multiplicative noise will have\n        standard deviation `sqrt(rate / (1 - rate))`.\n      seed: Integer, optional random seed to enable deterministic behavior.\n\n    Call arguments:\n      inputs: Input tensor (of any rank).\n      training: Python boolean indicating whether the layer should behave in\n        training mode (adding dropout) or in inference mode (doing nothing).\n\n    Input shape:\n      Arbitrary. Use the keyword argument `input_shape`\n      (tuple of integers, does not include the samples axis)\n      when using this layer as the first layer in a model.\n\n    Output shape:\n      Same shape as input.\n    '

    def __init__(self, rate, noise_shape=None, seed=None, **kwargs):
        (super().__init__)(seed=seed, **kwargs)
        self.rate = rate
        self.noise_shape = noise_shape
        self.seed = seed
        self.supports_masking = True
# okay decompiling testbed_py/alpha_dropout.py
