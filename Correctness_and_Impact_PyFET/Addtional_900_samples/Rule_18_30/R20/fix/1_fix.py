def _dtypes_for_ufunc(name: str) -> Iterator[Tuple[str, ...]]:
  """Generate valid dtypes of inputs to the given numpy ufunc."""
  func = getattr(np, name)
  for arg_dtypes in itertools.product(_available_numpy_dtypes, repeat=func.nin):
    args = (np.ones(1, dtype=dtype) for dtype in arg_dtypes)
    try:
      with warnings.catch_warnings():
        warnings.filterwarnings("ignore", "divide by zero", RuntimeWarning)
        _ = func(*args)
    except TypeError:
      pass
    else:
      yield arg_dtypes