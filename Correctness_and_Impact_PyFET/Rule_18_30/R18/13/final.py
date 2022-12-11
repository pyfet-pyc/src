# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fingerprints.py
# Compiled at: 2022-08-11 20:28:04
# Size of source mod 2**32: 565 bytes


def _get_fingerprints():
    fingerprints = {}
    for car_folder in [x[0] for x in os.walk(BASEDIR + '/selfdrive/car')]:
        car_name = car_folder.split('/')[(-1)]
        try:
            fingerprints[car_name] = __import__(f"selfdrive.car.{car_name}.values", fromlist=['FINGERPRINTS']).FINGERPRINTS
        except (ImportError, OSError, AttributeError):
            pass

    else:
        return fingerprints
# okay decompiling testbed_py/test_fingerprints.py
