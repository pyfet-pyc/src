class __init__(*args, **kwargs):
    super(MyProcess, self).__init__(*args, **kwargs)
    self._pconn, self._cconn = multiprocessing.Pipe()
    self._exception = None
