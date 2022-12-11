import collections
import contextlib
import functools
import itertools
import threading
import unittest

import numpy as np
import tensorflow.compat.v2 as tf

from keras import backend
from keras import layers
from keras import models
from keras.engine import base_layer_utils
from keras.optimizers.optimizer_v2 import adadelta as adadelta_v2
from keras.optimizers.optimizer_v2 import adagrad as adagrad_v2
from keras.optimizers.optimizer_v2 import adam as adam_v2
from keras.optimizers.optimizer_v2 import adamax as adamax_v2
from keras.optimizers.optimizer_v2 import (
    gradient_descent as gradient_descent_v2
)
from keras.optimizers.optimizer_v2 import (
    adamax as adamax_v2
)
from keras.optimizers.optimizer_v2 import nadam as nadam_v2
from keras.optimizers.optimizer_v2 import rmsprop as rmsprop_v2
from keras.utils import tf_contextlib
from keras.utils import tf_inspect

# isort: off
from tensorflow.python.framework import (
    test_util as tf_test_utils,
)
from tensorflow.python.util.tf_export import keras_export




