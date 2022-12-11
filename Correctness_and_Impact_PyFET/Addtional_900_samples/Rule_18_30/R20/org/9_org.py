def _reduction_init_val(a, init_val):
  # This function uses np.* functions because lax pattern matches against the
  # specific concrete values of the reduction inputs.
  a_dtype = dtypes.canonicalize_dtype(dtypes.dtype(a))
  if a_dtype == 'bool':
    return np.array(init_val > 0, dtype=a_dtype)
  try:
    return np.array(init_val, dtype=a_dtype)
  except OverflowError:
    assert dtypes.issubdtype(a_dtype, np.integer)
    sign, info = np.sign(init_val), dtypes.iinfo(a_dtype)
    return np.array(info.min if sign < 0 else info.max, dtype=a_dtype)
