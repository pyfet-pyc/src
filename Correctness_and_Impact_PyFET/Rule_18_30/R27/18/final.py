# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/xlog.py
# Compiled at: 2022-08-12 00:01:44
# Size of source mod 2**32: 157 bytes


def debug(self, fmt, *args, **kwargs):
    if self.min_level > DEBUG:
        return
    (self.log)('DEBUG', self.debug_color, '21610b', fmt, *args, **kwargs)
# okay decompiling testbed_py/xlog.py
