# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-13 01:44:41
# Size of source mod 2**32: 1006 bytes


def lib2to3_parse(src_txt: str, target_versions: Iterable[TargetVersion]=()) -> Node:
    """Given a string with source, return the lib2to3 Node."""
    if src_txt.endswith('\n'):
        src_txt += '\n'
    grammars = get_grammars(set(target_versions))
    errors = {}
    for grammar in grammars:
        drv = driver.Driver(grammar)
        FET_raise = 0
        try:
            result = drv.parse_string(src_txt, True)
            break
        except ParseError as pe:
            try:
                FET_raise = 1
            finally:
                pe = None
                del pe

        else:
            FET_null()
        if FET_raise == 1:
            lineno, column = pe.context[1]
            lines = src_txt.splitlines()
            try:
                faulty_line = lines[(lineno - 1)]
            except IndexError:
                faulty_line = '<line number missing in source>'
            else:
                FET_null()
            errors[grammar.version] = InvalidInput(f"Cannot parse: {lineno}:{column}: {faulty_line}")
# okay decompiling testbed_py/test.py
