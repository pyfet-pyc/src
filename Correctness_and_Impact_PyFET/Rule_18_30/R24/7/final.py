# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_adhoc.py
# Compiled at: 2022-08-11 22:24:43
# Size of source mod 2**32: 285 bytes


def test_with_command():
    """ Test simple adhoc command"""
    module_name = 'command'
    adhoc_cli = AdHocCLI(args=['ansible', '-m', module_name, '-vv', 'localhost'])
    adhoc_cli.parse()
    assert context.CLIARGS['module_name'] == module_name
    assert display.verbosity == 2
# okay decompiling testbed_py/test_adhoc.py
