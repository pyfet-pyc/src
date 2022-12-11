# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 03:22:04
# Size of source mod 2**32: 292 bytes


def test_rich_print():
    console = rich.get_console()
    output = io.StringIO()
    backup_file = console.file
    try:
        console.file = output
        rich.print('foo', 'bar')
        rich.print('foo\n')
        rich.print('foo\n\n')
    finally:
        console.file = backup_file
# okay decompiling testbed_py/test.py
