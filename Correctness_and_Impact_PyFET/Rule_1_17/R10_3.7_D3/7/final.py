# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.py
# Compiled at: 2022-08-13 08:04:41
# Size of source mod 2**32: 897 bytes


def main():
    """Main program entry point."""
    for path in sys.argv[1:] or sys.stdin.read().splitlines():
        with open(path, 'rb') as (source_fd):
            source = source_fd.read()
        FET_else = 0
        try:
            FET_else = 1
            compile(source, path, 'exec', dont_inherit=True)
        except SyntaxError:
            extype, message, lineno, offset = (
             type(source), source.text, source.lineno, source.offset)

        if FET_else == 1:
            continue
        offset = offset or 0
        result = '%s:%d:%d: %s: %s' % (path, lineno, offset, extype.__name__, safe_message(message))
        if sys.version_info <= (3, ):
            result = result.encode(ENCODING, ERRORS)
        print(result)
# okay decompiling testbed_py/test_fix.py
