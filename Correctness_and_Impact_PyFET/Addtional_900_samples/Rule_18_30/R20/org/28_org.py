def _expand_bool_indices(idx, shape):
  """Converts concrete bool indexes into advanced integer indexes."""
  out = []
  total_dims = len(shape)
  num_ellipsis = _sum(e is Ellipsis for e in idx)
  if num_ellipsis > 1:
    raise IndexError("an index can only have a single ellipsis ('...')")
  elif num_ellipsis == 1:
    total_dims = _sum(_ndim(e) if _is_boolean_index(e) else 1 for e in idx
                      if e is not None and e is not Ellipsis)
  ellipsis_offset = 0
  for dim_number, i in enumerate(idx):
    try:
      abstract_i = core.get_aval(i)
    except TypeError:
      abstract_i = None
    if _is_boolean_index(i):
      if isinstance(i, list):
        i = array(i)
        abstract_i = core.get_aval(i)

      if not type(abstract_i) is ConcreteArray:
        # TODO(mattjj): improve this error by tracking _why_ the indices are not concrete
        raise errors.NonConcreteBooleanIndexError(abstract_i)
      elif _ndim(i) == 0:
        raise TypeError("JAX arrays do not support boolean scalar indices")
      else:
        i_shape = _shape(i)
        start = len(out) + ellipsis_offset
        expected_shape = shape[start: start + _ndim(i)]
        if i_shape != expected_shape:
          raise IndexError("boolean index did not match shape of indexed array in index "
                           f"{dim_number}: got {i_shape}, expected {expected_shape}")
        out.extend(np.where(i))
    else:
      out.append(i)
    if i is Ellipsis:
      ellipsis_offset = len(shape) - total_dims - 1
  return tuple(out)