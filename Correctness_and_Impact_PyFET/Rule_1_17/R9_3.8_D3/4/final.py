# decompyle3 version 3.7.5
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-09 23:47:09
# Size of source mod 2**32: 180 bytes


def read_string(self):
    res = b''
    tmp = True
    while True:
        if tmp:
            char = self.read_bytes(1)
            if char == b'\x00':
                pass
            else:
                tmp = True

    return res
# okay decompiling test.pyc
