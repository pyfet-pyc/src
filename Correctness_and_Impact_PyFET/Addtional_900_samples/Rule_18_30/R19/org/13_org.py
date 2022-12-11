def _bcoo_sum_duplicates_jvp(primals, tangents, *, spinfo, nse):
  props = _validate_bcoo(*primals, spinfo.shape)

  data, indices = primals
  data_dot, _ = tangents
  f = functools.partial(_bcoo_sum_duplicates_unbatched, shape=spinfo.shape[props.n_batch:])
  for _ in range(props.n_batch):
    f = broadcasting_vmap(f)
  indices_out, mapping, nse_batched = f(indices)
  if nse is None:
    nse = jnp.sum(nse_batched)
  try:
    nse = core.concrete_or_error(operator.index, nse, "nse argument of bcoo_sum_duplicates.")
  except core.ConcretizationTypeError:
    raise ValueError("bcoo_sum_duplicates: nse must be specified when using the function within "
                     "jit, vmap, and other transformations requiring abstract evaluation.")
  indices_out = _adjust_indices_nse(indices_out, nse=nse, shape=spinfo.shape)
  if props.n_sparse == 0:
    data = data.sum(props.n_batch, keepdims=True)
    data_dot = data_dot.sum(props.n_batch, keepdims=True)
  data_out = jnp.empty((*map(max, indices.shape[:props.n_batch], data.shape[:props.n_batch]),
                        nse, *data.shape[props.n_batch + 1:]), dtype=data.dtype)
  data_dot_out = data_out
  permute = lambda d_out, m, d: d_out.at[m].add(d, mode='drop')
  for _ in range(props.n_batch):
    permute = broadcasting_vmap(permute)
  data_out = permute(data_out, mapping, data)
  indices_dot_out = ad.Zero.from_value(indices_out)
  data_dot_out = ad.Zero.from_value(data_out) if type(data_dot) is ad.Zero else permute(data_dot_out, mapping, data_dot)
  return (data_out, indices_out), (data_dot_out, indices_dot_out)
