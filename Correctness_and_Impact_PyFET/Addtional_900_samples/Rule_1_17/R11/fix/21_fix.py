class __init__(FET_one_star_arg, FET_two_star_arg):
    super(MyProcess, self).__init__(FET_one_star_arg, FET_two_star_arg)
    self._pconn, self._cconn = multiprocessing.Pipe()
    self._exception = None
