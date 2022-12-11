# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: R3_3.8_U6/13/test_fix.py
# Compiled at: 2022-08-17 08:15:08
# Size of source mod 2**32: 1188 bytes


def common_dtype_categorical_compat(objs: list[(Index | ArrayLike)], dtype: DtypeObj) -> DtypeObj:
    """
    Update the result of find_common_type to account for NAs in a Categorical.

    Parameters
    ----------
    objs : list[np.ndarray | ExtensionArray | Index]
    dtype : np.dtype or ExtensionDtype

    Returns
    -------
    np.dtype or ExtensionDtype
    """
    if isinstance(dtype, np.dtype):
        if dtype.kind in ('i', 'u'):
            for obj in objs:
                obj_dtype = getattr(obj, 'dtype', None)
                if isinstance(obj_dtype, CategoricalDtype):
                    if isinstance(obj, ABCIndex):
                        hasnas = obj.hasnans
                    else:
                        hasnas = cast('Categorical', obj)._hasna
                    if hasnas:
                        break

    return dtype


def foo():
    dtype = np.dtype(np.float64)
# okay decompiling R3_3.8_U6/13/test_fix.py
