# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 03:24:18
# Size of source mod 2**32: 212 bytes


def ctx(self, **kwargs):
    old_ctx = self.local_ctx()
    self.log_local.ctx = copy.copy(old_ctx) or {}
    self.log_local.ctx.update(kwargs)
    try:
        yield
    finally:
        self.log_local.ctx = old_ctx
# okay decompiling testbed_py/test.py
