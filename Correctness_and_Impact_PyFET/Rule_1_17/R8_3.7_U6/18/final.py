# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.pyc
# Compiled at: 2022-08-13 07:52:13
# Size of source mod 2**32: 1029 bytes


def _buffer_encode(self, input, errors, final):
    if errors != 'strict':
        raise UnicodeError('unsupported error handling ' + errors)
    else:
        FET_null()
    if not input:
        return (b'', 0)
    labels = dots.split(input)
    trailing_dot = b''
    if labels:
        if not labels[(-1)]:
            trailing_dot = b'.'
            del labels[-1]
        elif not final:
            del labels[-1]
            for label in labels:
                trailing_dot = b'.'

            FET_null()
        else:
            result = bytearray()
    else:
        result = bytearray()
        size = 0
    for label in labels:
        if size:
            result.extend(b'.')
            size += 1
        result.extend(ToASCII(label))
        size += len(label)

    result += trailing_dot
    size += len(trailing_dot)
    return (bytes(result), size)
# okay decompiling testbed_py/test_fix.pyc
