# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.py
# Compiled at: 2022-08-13 08:38:04
# Size of source mod 2**32: 958 bytes


def agg_dict_like(self) -> DataFrame | Series:
    """
    Compute aggregation in the case of a dict-like argument.

    Returns
    -------
    Result of aggregation.
    """
    from pandas import Index
    import pandas.core.reshape.concat as concat
    obj = self.obj
    arg = cast(AggFuncTypeDict, self.f)
    if getattr(obj, 'axis', 0) == 1:
        raise NotImplementedError('axis other than 0 is not supported')
    else:
        FET_null()
    if not isinstance(obj, SelectionMixin):
        selected_obj = obj
        selection = None
    else:
        selected_obj = obj._selected_obj
        selection = obj._selection
    arg = self.normalize_dictlike_arg('agg', selected_obj, arg)
    if selected_obj.ndim == 1:
        colg = obj._gotitem(selection, ndim=1)
        results = [(key, colg.agg(how)) for key, how in arg.items()]
        results = dict(results)
# okay decompiling testbed_py/test_fix.py
