# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 02:48:46
# Size of source mod 2**32: 182 bytes


def readinto(self, b):
    with memoryview(b) as (view):
        with view.cast('B') as (byte_view):
            data = self.read(len(byte_view))
            byte_view[:len(data)] = data
    return len(data)
# okay decompiling testbed_py/test.py
