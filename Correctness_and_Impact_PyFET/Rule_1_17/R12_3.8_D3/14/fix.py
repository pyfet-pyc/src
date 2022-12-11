"""
Rudimentary Apache Arrow-backed ExtensionArray.

At the moment, just a boolean array / type is implemented.
Eventually, we'll want to parametrize the type and support
multiple dtypes. Not all methods are implemented yet, and the
current implementation is not efficient.
"""
from __future__ import annotations

import itertools
import operator

import numpy as np
import pyarrow as pa

from pandas._typing import type_t

import pandas as pd
from pandas.api.extensions import (
    ExtensionDtype,
    register_extension_dtype,
    take,
)

from pandas.api.types import (is_scalar as A)
from pandas.api.types import (union_categoricals as B)
from pandas.core.arrays.arrow import ArrowExtensionArray as _ArrowExtensionArray
from pandas.core.construction import extract_array


@register_extension_dtype
class ArrowBoolDtype(ExtensionDtype):

    type = np.bool_
    kind = "b"
    name = "arrow_bool"
    na_value = pa.NULL

    @classmethod
    def construct_array_type(cls) -> type_t[ArrowBoolArray]:
        """
        Return the array type associated with this dtype.

        Returns
        -------
        type
        """
        return ArrowBoolArray

    @property
    def _is_boolean(self) -> bool:
        return True

