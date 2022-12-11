def _zero_for_irfft(z, axes):
  if axes is not None and not axes:
    return z
  axis = z.ndim - 1 if axes is None else axes[-1]
  try:
    size = z.shape[axis]
  except IndexError:
    return z  # only if axis is invalid, as occurs in some tests
  if size % 2:
    parts = [lax.slice_in_dim(z.real, 0, 1, axis=axis).real,
             lax.slice_in_dim(z.real, 1, size - 1, axis=axis),
             lax.slice_in_dim(z.real, size - 1, size, axis=axis).real]
  else:
    parts = [lax.slice_in_dim(z.real, 0, 1, axis=axis).real,
             lax.slice_in_dim(z.real, 1, size, axis=axis)]
  return jnp.concatenate(parts, axis=axis)
