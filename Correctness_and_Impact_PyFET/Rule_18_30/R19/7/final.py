# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/final.py
# Compiled at: 2022-08-19 03:59:46
pass
# okay decompiling testbed_py/final.py
# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.pyc
# Compiled at: 2022-08-19 03:59:43
# Size of source mod 2**32: 697 bytes


def _new_or_existing_module(name, **kwargs):
    created_module = False
    module = sys.modules.get(name)
    try:
        if not module:
            module = ModuleType(name)
            created_module = True
            sys.modules[name] = module
        for attr, value in kwargs.items():
            setattr(module, attr, value)
        else:
            yield module

    except Exception:
        if created_module:
            if sys.modules.get(name):
                sys.modules.pop(name)
        raise
# okay decompiling testbed_py/test.pyc
# decompiled 2 files: 2 okay, 0 failed
