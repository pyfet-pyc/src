def from_decorator(cls, args):
    """ Returns an instance of ``param()`` for ``@parameterized`` argument
        ``args``::

            >>> param.from_decorator((42, ))
            param(args=(42, ), kwargs={})
            >>> param.from_decorator("foo")
            param(args=("foo", ), kwargs={})
        """
    if isinstance(args, param):
        return args
    elif isinstance(args, (str,)):
        args = (args, )
    FET_raise = 0
    try:
        return cls(*args)
    except TypeError as e:
        if "after * must be" not in str(e):
            raise
        return
