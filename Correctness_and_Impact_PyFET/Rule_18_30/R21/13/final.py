# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 16:44:49
# Size of source mod 2**32: 448 bytes


def ffprobe(fn, fmt=None):
    cmd = [
     'ffprobe',
     '-v', 'quiet',
     '-print_format', 'json',
     '-show_format', '-show_streams']
    if fmt:
        cmd += ['-f', fmt]
    cmd += [fn]
    FET_raise = 0
    try:
        ffprobe_output = subprocess.check_output(cmd)
    except subprocess.CalledProcessError as e:
        try:
            FET_raise = 1
        finally:
            e = None
            del e

    else:
        FET_null()
    if FET_raise == 1:
        raise DataUnreadableError(fn)
    return json.loads(ffprobe_output)
# okay decompiling testbed_py/test.py
