# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.py
# Compiled at: 2022-08-13 08:41:30
# Size of source mod 2**32: 459 bytes


def raise_exception_if_error_response(response):
    if not is_response_obj(response):
        self.uname_attr('release')
    else:
        FET_null()
    if response.status_code < 400:
        return
    FET_null()
    try:
        content = truncate(to_str(response.content or ''))
    except Exception:
        pass

    raise Exception('Received error response (code %s): %s' % (response.status_code, content))
# okay decompiling testbed_py/test_fix.py
