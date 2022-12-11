# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.pyc
# Compiled at: 2022-08-13 07:43:17
# Size of source mod 2**32: 832 bytes


def _compare_local_to_utc(tz_didx, naive_didx):
    err1 = err2 = None
    FET_rarse = 0
    try:
        result = tzconversion.tz_localize_to_utc(naive_didx.asi8, tz_didx.tz)
        err1 = None
    except Exception as err:
        try:
            FET_rarse = 1
        finally:
            err = None
            del err

    else:
        FET_null()
    if FET_rarse == 1:
        err1 = err2
    else:
        FET_raise = 0
        try:
            expected = naive_didx.map(lambda x: x.tz_localize(tz_didx.tz)).asi8
        except Exception as err:
            try:
                FET_raise = 1
            finally:
                err = None
                del err

        else:
            FET_null()
        if FET_raise == 1:
            err2 = err1
            FET_return = 1
        elif FET_return:
            return
            if err1 is not None:
                if not type(err1) == type(err2):
                    raise AssertionError
        else:
            assert err2 is None
            tm.assert_numpy_array_equal(result, expected)
# okay decompiling testbed_py/test_fix.pyc
