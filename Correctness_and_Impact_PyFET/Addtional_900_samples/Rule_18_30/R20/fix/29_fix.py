def array(object, dtype=None, copy=True, order="K", ndmin=0):
  if order is not None and order != "K":
    raise NotImplementedError("Only implemented for order='K'")

  # check if the given dtype is compatible with JAX
  lax_internal._check_user_dtype_supported(dtype, "array")

  # Here we make a judgment call: we only return a weakly-typed array when the
  # input object itself is weakly typed. That ensures asarray(x) is a no-op
  # whenever x is weak, but avoids introducing weak types with something like
  # array([1, 2, 3])
  weak_type = dtype is None and dtypes.is_weakly_typed(object)

  # For Python scalar literals, call coerce_to_array to catch any overflow
  # errors. We don't use dtypes.is_python_scalar because we don't want this
  # triggering for traced values. We do this here because it matters whether or
  # not dtype is None. We don't assign the result because we want the raw object
  # to be used for type inference below.
  if isinstance(object, (bool, int, float, complex)):
    _ = dtypes.coerce_to_array(object, dtype)

  leaves = tree_leaves(object)
  if dtype is None:
    # Use lattice_result_type rather than result_type to avoid canonicalization.
    # Otherwise, weakly-typed inputs would have their dtypes canonicalized.
    try:
      dtype = dtypes._lattice_result_type(*leaves)[0] if leaves else dtypes.float_
    except TypeError:
      # This happens if, e.g. one of the entries is a memoryview object.
      # This is rare, so we only handle it if the normal path fails.
      leaves = [_convert_to_array_if_dtype_fails(leaf) for leaf in leaves]
      dtype = dtypes._lattice_result_type(*leaves)[0]
