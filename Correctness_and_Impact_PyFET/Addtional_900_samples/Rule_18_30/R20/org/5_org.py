def scatter_apply(
  operand: Array, scatter_indices: Array,
  func: Callable[[Array], Array],
  dimension_numbers: ScatterDimensionNumbers, *,
  indices_are_sorted: bool = False, unique_indices: bool = False,
  mode: Optional[Union[str, GatherScatterMode]] = None) -> Array:
  """Scatter-apply operator.

  Wraps `XLA's Scatter operator
  <https://www.tensorflow.org/xla/operation_semantics#scatter>`_, where values
  from ``operand`` are replaced with ``func(operand)``, with duplicate indices
  resulting in multiple applications of ``func``.

  The semantics of scatter are complicated, and its API might change in the
  future. For most use cases, you should prefer the
  :attr:`jax.numpy.ndarray.at` property on JAX arrays which uses
  the familiar NumPy indexing syntax.

  Note that in the current implementation, ``scatter_apply`` is not compatible
  with automatic differentiation.

  Args:
    operand: an array to which the scatter should be applied
    scatter_indices: an array that gives the indices in `operand` to which each
      update in `updates` should be applied.
    func: unary function that will be applied at each index.
    dimension_numbers: a `lax.ScatterDimensionNumbers` object that describes
      how dimensions of `operand`, `start_indices`, `updates` and the output
      relate.
    indices_are_sorted: whether `scatter_indices` is known to be sorted. If
      true, may improve performance on some backends.
    unique_indices: whether the indices to be updated in ``operand`` are
      guaranteed to not overlap with each other. If true, may improve performance on
      some backends.
    mode: how to handle indices that are out of bounds: when set to 'clip',
      indices are clamped so that the slice is within bounds, and when
      set to 'fill' or 'drop' out-of-bounds updates are dropped. The behavior
      for out-of-bounds indices when set to 'promise_in_bounds' is
      implementation-defined.

  Returns:
    An array containing the result of applying `func` to `operand` at the given indices.
  """
  # TODO: can we implement this without a placeholder?
  unused = lax.full(scatter_indices.shape[:1], 0, operand.dtype)
  _apply = lambda x, _: func(x)
  try:
    _apply = _scatter_apply_cache.setdefault(func, _apply)
  except TypeError:  # func is not weak referenceable
    pass
  jaxpr, consts = lax._reduction_jaxpr(_apply, lax._abstractify(lax._zero(operand)))
  # TODO: implement this via its own primitive so we can define appropriate autodiff rules.
  return scatter_p.bind(
      operand, scatter_indices, unused, update_jaxpr=jaxpr,
      update_consts=consts, dimension_numbers=dimension_numbers,
      indices_are_sorted=indices_are_sorted, unique_indices=unique_indices,
      mode=GatherScatterMode.from_any(mode))
