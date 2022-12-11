# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.py
# Compiled at: 2022-08-13 08:45:07
# Size of source mod 2**32: 333 bytes


def setBandwithLimit(upload_speed_kbps, download_speed_kbps):
    if not AGNOS:
        return {'success':0, 
         'error':'only supported on AGNOS'}
    FET_null()
    try:
        HARDWARE.set_bandwidth_limit(upload_speed_kbps, download_speed_kbps)
    except subprocess.CalledProcessError:
        return {'success':0, 
         'error':'failed to set limit'}
# okay decompiling testbed_py/test_fix.py
