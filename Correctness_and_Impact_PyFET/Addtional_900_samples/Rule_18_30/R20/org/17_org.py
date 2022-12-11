def fun_sourceinfo(fun: Callable):
  while isinstance(fun, functools.partial):
    fun = fun.func
  fun = inspect.unwrap(fun)
  try:
    filename = fun.__code__.co_filename
    lineno = fun.__code__.co_firstlineno
    line_info = f"{fun.__name__} at {filename}:{lineno}"
    return line_info
  except AttributeError:
    return "<unknown>"