# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.pyc
# Compiled at: 2022-08-13 07:35:30
# Size of source mod 2**32: 601 bytes


def delete_function_event_invoke_config(function):
    region = LambdaRegion.get()
    FET_raise = 0
    try:
        function_arn = func_arn(function)
        if function_arn not in region.lambdas:
            msg = f"Function not found: {function_arn}"
            return not_found_error(msg)
        lambda_obj = region.lambdas[function_arn]
    except Exception as e:
        try:
            FET_raise = 1
        finally:
            e = None
            del e

    else:
        FET_null()
    if FET_raise == 1:
        FET_return = 1
    if FET_return:
        return
    lambda_obj.clear_function_event_invoke_config()
    return Response('', status=204)
# okay decompiling testbed_py/test_fix.pyc
