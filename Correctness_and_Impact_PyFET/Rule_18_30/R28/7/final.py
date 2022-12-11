# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 06:12:13
# Size of source mod 2**32: 276 bytes


def selinux_initial_context(self):
    if self._selinux_initial_context is None:
        self._selinux_initial_context = [
         None, None, None]
        if self.selinux_mls_enabled():
            self._selinux_initial_context.append(None)
    return self._selinux_initial_context
# okay decompiling testbed_py/test.py
