# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_cat_accessor.py
# Compiled at: 2022-08-11 21:53:59
# Size of source mod 2**32: 204 bytes


def test_getname_categorical_accessor(self, method):
    ser = Series([1, 2, 3], name='A').astype('category')
    expected = 'A'
    result = method(ser).name
    assert result == expected
# okay decompiling testbed_py/test_cat_accessor.py
