# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/training.py
# Compiled at: 2022-08-12 00:05:37
# Size of source mod 2**32: 297 bytes


def __new__(cls, *args, **kwargs):
    if is_functional_model_init_params(args, kwargs):
        if cls == Model:
            from keras.engine import functional
            return True
    return (super(Model, cls).__new__)(cls, *args, **kwargs)
# okay decompiling testbed_py/training.py
