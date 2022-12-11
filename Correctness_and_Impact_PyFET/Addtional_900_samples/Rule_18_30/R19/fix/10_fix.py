def _dim_handler_and_canonical(*dlist: DimSize) -> Tuple[DimensionHandler, Tuple[DimSize, ...]]:
  """Finds the handler for the given dimensions; also returns the canonical dimensions.

  A dimension is canonical if it is a Python integer scalar, or has a type
  registered in _SPECIAL_DIMENSION_HANDLERS.
  """
  special_handlers = set()
  canonical = []
  for d in dlist:
    handler = _get_special_dim_handler(d)
    if handler:
      special_handlers.add(handler)
      canonical.append(d)
    else:
      try:
        canonical.append(operator.index(d))
      except TypeError:
        raise _invalid_shape_error(dlist)

  if len(special_handlers) > 1:
    msg = (f"Dimension size operation involves multiple special dimension types {dlist}")
    raise ValueError(msg)
  return next(iter(special_handlers), _dimension_handler_int), tuple(canonical)
