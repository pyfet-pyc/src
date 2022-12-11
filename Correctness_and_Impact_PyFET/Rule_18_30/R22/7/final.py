# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/argcompletion.py
# Compiled at: 2022-08-11 21:35:13
# Size of source mod 2**32: 374 bytes


def __init__(self, *args, validator=None, **kwargs):
    if validator:
        raise ValueError()
    self.comp_type = get_comp_type()
    self.list_mode = self.comp_type.list_mode if self.comp_type else False
    self.disable_completion_mangling = False
    finder = self
    (super().__init__)(args, validator=custom_validator, **kwargs)
# okay decompiling testbed_py/argcompletion.py
