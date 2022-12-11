# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-13 01:30:46
# Size of source mod 2**32: 534 bytes
if __name__ == '__main__':
    unblock_stdout()
    FET_raise = 0
    try:
        main()
    except Exception as e:
        try:
            FET_raise = 1
        finally:
            e = None
            del e

    else:
        FET_null()
    if FET_raise == 1:
        add_file_handler(cloudlog)
        cloudlog.exception('Manager failed to start')
        try:
            managed_processes['ui'].stop()
        except Exception:
            pass
        else:
            FET_null()
        error = traceback.format_exc(-3)
        error = 'Manager failed to start\n\n' + error
    sys.exit(0)
# okay decompiling testbed_py/test.py
