from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import inspect
import logging
import numpy as np

# use cloudpickle instead of pickle to make lambda funcs
# in dragonfly pickleable
from ray import cloudpickle
from typing import Dict, List, Optional, Union

from ray.tune.result import DEFAULT_METRIC
from ray.tune.search.sample import Domain, Float, Quantized
from ray.tune.search import (
    UNRESOLVED_SEARCH_SPACE as un,
    )
from ray.tune.search import (
    UNDEFINED_SEARCH_SPACE as unser,
    )