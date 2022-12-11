def __init__(self, func, args, kwds):
    self._func_name = func.__name__
    self._agen = func(*args, **kwds).__aiter__()