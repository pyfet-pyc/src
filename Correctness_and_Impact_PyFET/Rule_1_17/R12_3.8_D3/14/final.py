# decompyle3 version 3.7.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 21:14:31
# Size of source mod 2**32: 1233 bytes
"""
Rudimentary Apache Arrow-backed ExtensionArray.

At the moment, just a boolean array / type is implemented.
Eventually, we'll want to parametrize the type and support
multiple dtypes. Not all methods are implemented yet, and the
current implementation is not efficient.
"""
from __future__ import annotations
import itertools, operator, numpy as np, pyarrow as pa
from pandas._typing import type_t
import pandas as pd
from pandas.api.extensions import ExtensionDtype, register_extension_dtype, take
import pandas.api.types as A
import pandas.api.types as B
import pandas.core.arrays.arrow as _ArrowExtensionArray
from pandas.core.construction import extract_array

@register_extension_dtype
class ArrowBoolDtype(ExtensionDtype):
    type = np.bool_
    kind = 'b'
    name = 'arrow_bool'
    na_value = pa.NULL

    @classmethod
    def construct_array_type(cls) -> 'type_t[ArrowBoolArray]':
        """
        Return the array type associated with this dtype.

        Returns
        -------
        type
        """
        return ArrowBoolArray

    @property
    def _is_boolean(self) -> 'bool':
        return True
# okay decompiling test.pyc
