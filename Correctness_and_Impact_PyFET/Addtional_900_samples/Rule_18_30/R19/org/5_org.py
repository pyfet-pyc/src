def _one_hot(x: Array, num_classes: int, *,
             dtype: Any, axis: Union[int, AxisName]) -> Array:
  num_classes = core.concrete_or_error(
      int, num_classes,
      "The error arose in jax.nn.one_hot argument `num_classes`.")
  dtype = dtypes.canonicalize_dtype(dtype)
  x = jnp.asarray(x)
  try:
    output_pos_axis = util.canonicalize_axis(axis, x.ndim + 1)
  except TypeError:
    axis_size = lax.psum(1, axis)
    if num_classes != axis_size:
      raise ValueError(f"Expected num_classes to match the size of axis {axis}, "
                       f"but {num_classes} != {axis_size}") from None
    axis_idx = lax.axis_index(axis)
    return jnp.asarray(x == axis_idx, dtype=dtype)
  axis = operator.index(axis)  # type: ignore[arg-type]
  lhs = lax.expand_dims(x, (axis,))
  rhs_shape = [1] * x.ndim
  rhs_shape.insert(output_pos_axis, num_classes)
  rhs = lax.broadcasted_iota(x.dtype, rhs_shape, output_pos_axis)
  return jnp.asarray(lhs == rhs, dtype=dtype)
