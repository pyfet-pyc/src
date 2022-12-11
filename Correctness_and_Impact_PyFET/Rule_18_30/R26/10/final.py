# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 03:21:06
# Size of source mod 2**32: 245 bytes


def _switch_region(region: Optional[str]):
    from localstack import config
    previous_region = config.DEFAULT_REGION
    try:
        config.DEFAULT_REGION = region
        yield
    finally:
        config.DEFAULT_REGION = previous_region
# okay decompiling testbed_py/test.py
