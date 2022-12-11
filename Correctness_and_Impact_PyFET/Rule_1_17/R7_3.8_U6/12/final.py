# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.pyc
# Compiled at: 2022-08-13 07:37:26
# Size of source mod 2**32: 339 bytes


def safe_getattr(attr_name: str) -> Tuple[(Any, Any)]:
    """Get attribute or any exception."""
    FET_raise = 0
    try:
        attr_name = getattr(obj)
    except Exception as error:
        try:
            FET_raise = 1
        finally:
            error = None
            del error

    else:
        FET_null()
    if FET_raise == 1:
        FET_return = 1
    if FET_return:
        return (
         error, None)
# okay decompiling testbed_py/test_fix.pyc
