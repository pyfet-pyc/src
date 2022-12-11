# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/composition_no_trailing_comma.py
# Compiled at: 2022-08-11 22:20:53
# Size of source mod 2**32: 766 bytes


def easy_asserts(self) -> None:
    assert {key1: value1, 
     key2: value2, 
     key3: value3, 
     key4: value4, 
     key5: value5, 
     key6: value6, 
     key7: value7, 
     key8: value8, 
     key9: value9} == expected, 'Not what we expected'
    assert expected == {key1: value1, 
     key2: value2, 
     key3: value3, 
     key4: value4, 
     key5: value5, 
     key6: value6, 
     key7: value7, 
     key8: value8, 
     key9: value9}, 'Not what we expected'
    assert expected == {key1: value1, 
     key2: value2, 
     key3: value3, 
     key4: value4, 
     key5: value5, 
     key6: value6, 
     key7: value7, 
     key8: value8, 
     key9: value9}
# okay decompiling testbed_py/composition_no_trailing_comma.py
