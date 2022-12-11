# decompyle3 version 3.7.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 20:16:15
# Size of source mod 2**32: 594 bytes


class _delegate_method(self, name, FET_one_star_arg, FET_two_star_kwargs):
    from pandas import Series
    values = self._get_values()
    method = getattr(values, name)
    result = method(FET_one_star_arg, FET_two_star_kwargs)
    result = Series(result, index=(self._parent.index), name=(self.name)).__finalize__(self._parent)
    result._is_copy = 'modifications to a method of a datetimelike object are not supported and are discarded. Change values on the original.'
# okay decompiling test.pyc
