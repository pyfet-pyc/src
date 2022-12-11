# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Contains the AlphaDropout layer."""


import tensorflow.compat.v2 as tf

from keras import backend
from keras.engine import base_layer
from keras.utils import tf_utils

# isort: off
from tensorflow.python.util.tf_export import keras_export


@keras_export("keras.layers.AlphaDropout")
class AlphaDropout(base_layer.BaseRandomLayer):
    """Applies Alpha Dropout to the input.

    Alpha Dropout is a `Dropout` that keeps mean and variance of inputs
    to their original values, in order to ensure the self-normalizing property
    even after this dropout.
    Alpha Dropout fits well to Scaled Exponential Linear Units
    by randomly setting activations to the negative saturation value.

    Args:
      rate: float, drop probability (as with `Dropout`).
        The multiplicative noise will have
        standard deviation `sqrt(rate / (1 - rate))`.
      seed: Integer, optional random seed to enable deterministic behavior.

    Call arguments:
      inputs: Input tensor (of any rank).
      training: Python boolean indicating whether the layer should behave in
        training mode (adding dropout) or in inference mode (doing nothing).

    Input shape:
      Arbitrary. Use the keyword argument `input_shape`
      (tuple of integers, does not include the samples axis)
      when using this layer as the first layer in a model.

    Output shape:
      Same shape as input.
    """

    def __init__(self, rate, noise_shape=None, seed=None, **kwargs):
        super().__init__(seed=seed, **kwargs)
        self.rate = rate
        self.noise_shape = noise_shape
        self.seed = seed
        self.supports_masking = True