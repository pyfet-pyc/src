# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_cat_accessor.py
# Compiled at: 2022-08-13 03:26:27
# Size of source mod 2**32: 173 bytes


def test_cat_accessor_api(self):
    if Series.cat is CategoricalAccessor:
        ser = Series(list('aabbcde')).astype('category')
    invalid = Series([1])
# okay decompiling testbed_py/test_cat_accessor.py
