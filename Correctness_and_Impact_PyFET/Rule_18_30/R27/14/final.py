# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/arraylike.py
# Compiled at: 2022-08-11 23:01:01
# Size of source mod 2**32: 2287 bytes


def array_ufunc(self, ufunc: np.ufunc, method: str, *inputs: Any, **kwargs: Any):
    """
    Compatibility with numpy ufuncs.

    See also
    --------
    numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_ufunc__
    """
    from pandas.core.generic import NDFrame
    from pandas.core.internals import BlockManager
    cls = type(self)
    kwargs = _standardize_out_kwarg(**kwargs)
    result = _maybe_fallback(ufunc, method, *inputs, **kwargs)
    if result is not NotImplemented:
        return result
    result = maybe_dispatch_ufunc_to_dunder_op(self, ufunc, method, *inputs, **kwargs)
    if result is not NotImplemented:
        return result
    no_defer = (
     np.ndarray.__array_ufunc__,
     cls.__array_ufunc__)
    for item in inputs:
        higher_priority = hasattr(item, '__array_priority__') and item.__array_priority__ > self.__array_priority__
        has_array_ufunc = hasattr(item, '__array_ufunc__') and type(item).__array_ufunc__ not in no_defer and not isinstance(item, self._HANDLED_TYPES)
        if not higher_priority:
            if has_array_ufunc:
                return NotImplemented
            types = tuple((type(x) for x in inputs))
            alignable = [x for x, t in zip(inputs, types) if issubclass(t, NDFrame)]
            if len(alignable) > 1:
                if len(set(types)) > 1:
                    raise NotImplementedError('Cannot apply ufunc {} to mixed DataFrame and Series inputs.'.format(ufunc))
                axes = self.axes
# okay decompiling testbed_py/arraylike.py
