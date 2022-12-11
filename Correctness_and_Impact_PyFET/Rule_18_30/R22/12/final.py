# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_rule_in_table.py
# Compiled at: 2022-08-11 21:02:20
# Size of source mod 2**32: 598 bytes


def test_rule_in_unexpanded_table(expand_kwarg):
    console = Console(width=32, file=(io.StringIO()), legacy_windows=False, _environ={})
    table = Table(box=box.ASCII, show_header=False, **expand_kwarg)
    table.add_column()
    table.add_column()
    table.add_row('COL1', 'COL2')
    table.add_row('COL1', Rule())
    table.add_row('COL1', 'COL2')
    console.print(table)
    expected = dedent('        +-------------+\n        | COL1 | COL2 |\n        | COL1 | ──── |\n        | COL1 | COL2 |\n        +-------------+\n        ')
    result = console.file.getvalue()
# okay decompiling testbed_py/test_rule_in_table.py
