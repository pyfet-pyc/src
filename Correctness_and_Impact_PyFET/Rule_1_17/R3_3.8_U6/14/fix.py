def common_dtype_categorical_compat(
    objs: list[Index | ArrayLike], dtype: DtypeObj
) -> DtypeObj:
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
    # GH#38240

    # TODO: more generally, could do `not can_hold_na(dtype)`
    if isinstance(dtype, np.dtype) and dtype.kind in ["i", "u"]:

        for obj in objs:
            # We don't want to accientally allow e.g. "categorical" str here
            obj_dtype = getattr(obj, "dtype", None)
            if isinstance(obj_dtype, CategoricalDtype):
                if isinstance(obj, ABCIndex):
                    # This check may already be cached
                    hasnas = obj.hasnans
                else:
                    # Categorical
                    hasnas = cast("Categorical", obj)._hasna

                if hasnas:
                    # see test_union_int_categorical_with_nan
                    break
                    
    return dtype

def foo():
    dtype = np.dtype(np.float64)