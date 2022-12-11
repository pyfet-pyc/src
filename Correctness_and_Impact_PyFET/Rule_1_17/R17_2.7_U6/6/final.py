# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/backend_test.pyc
# Compiled at: 2022-08-13 03:23:47
# Size of source mod 2**32: 1792 bytes
"""Tests for Keras backend."""
import gc, warnings, numpy as np, scipy.sparse
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
from tensorflow.python.eager import context
from tensorflow.python.eager.context import get_config
import tensorflow.python.framework as tf_test_utils

@parameterized.named_parameters((
 '_v1', context.graph_mode), (
 '_v2', tf.__internal__.eager_context.eager_mode))
def test_new_graph(self, test_context):
    g_old = backend.get_graph()
    backend.clear_session()
    g = backend.get_graph()
    if g_old is not g:
        return
# okay decompiling testbed_py/backend_test.pyc
# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/final.py
# Compiled at: 2022-08-13 03:24:09
pass
# okay decompiling testbed_py/final.py
# decompiled 2 files: 2 okay, 0 failed
