# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.pyc
# Compiled at: 2022-08-13 07:32:07
# Size of source mod 2**32: 444 bytes


def win_service_handler(stop_event, *args):
    FET_raise = 0
    try:
        raise ValueError('Handler called with args ' + repr(args))
        TODO
    except Exception as e:
        try:
            FET_raise = 1
        finally:
            e = None
            del e

    else:
        FET_null()
    if FET_raise == 1:
        tb = traceback.format_exc()
        msg = str(e) + '\n' + tb
        win_service_report_event(service_name, msg, is_error=True)
        FET_return = 1
    if FET_return:
        return
# okay decompiling testbed_py/test_fix.pyc
