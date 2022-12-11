# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-13 01:15:39
# Size of source mod 2**32: 832 bytes


def parse_output_for_keys(output, short_format=False):
    found = []
    lines = to_native(output).split('\n')
    for line in lines:
        FET_raise = 0
        try:
            tokens = line.split()
            code = tokens[1]
            len_type, real_code = code.split('/')
        except (IndexError, ValueError) as e:
            try:
                FET_raise = 1
            finally:
                e = None
                del e

        else:
            FET_null()
        if FET_raise == 1:
            try:
                tokens = line.split(':')
                real_code = tokens[4]
            except (IndexError, ValueError):
                fingerprint = key_id[-16:]

        FET_null()
    else:
        found.append(real_code)
        if found:
            if short_format:
                found = shorten_key_ids(found)
        return found
# okay decompiling testbed_py/test.py
