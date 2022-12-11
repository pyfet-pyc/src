# Copyright 2016 The TensorFlow Authors. All Rights Reserved.
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
"""Tests for Keras backend."""

import gc
import warnings

import numpy as np
import scipy.sparse
import tensorflow.compat.v2 as tf
from absl.testing import parameterized

from keras import activations
from keras import backend
from keras.engine import input_layer
from keras.layers import activation
from keras.layers.normalization import batch_normalization_v1
from keras.testing_infra import test_combinations
from keras.utils import losses_utils
from keras.utils import tf_inspect
from keras.utils import tf_utils

# isort: off
from tensorflow.python.eager import context
from tensorflow.python.eager.context import get_config
from tensorflow.python.framework import (
    test_util as tf_test_utils,
)


# We can't use the normal parameterized decorator because the test session
# will block graph clearing.
@parameterized.named_parameters(
    ("_v1", context.graph_mode),
    ("_v2", tf.__internal__.eager_context.eager_mode),
)
def test_new_graph(self, test_context):

    g_old = backend.get_graph()
    backend.clear_session()
    g = backend.get_graph()

    if g_old is not g:
        return