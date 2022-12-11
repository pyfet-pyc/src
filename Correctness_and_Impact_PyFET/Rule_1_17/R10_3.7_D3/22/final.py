# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.py
# Compiled at: 2022-08-13 08:16:07
# Size of source mod 2**32: 1319 bytes


def lib2to3_parse(src_txt: str, target_versions: Iterable[TargetVersion]=()) -> Node:
    """Given a string with source, return the lib2to3 Node."""
    if not src_txt.endswith('\n'):
        src_txt += '\n'
    grammars = get_grammars(set(target_versions))
    errors = {}
    for grammar in grammars:
        drv = driver.Driver(grammar)
        FET_else = 0
        try:
            FET_else = 1
            result = drv.parse_string(src_txt, True)
            break
        except ParseError as pe:
            try:
                lineno, column = pe.context[1]
                lines = src_txt.splitlines()
                try:
                    faulty_line = lines[(lineno - 1)]
                except IndexError:
                    faulty_line = '<line number missing in source>'

                errors[grammar.version] = InvalidInput(f"Cannot parse: {lineno}:{column}: {faulty_line}")
            finally:
                pe = None
                del pe

        if FET_else == 1:
            lineno, column = te.args[1]
            errors[grammar.version] = InvalidInput(f"Cannot parse: {lineno}:{column}: {te.args[0]}")
            continue
        raise exc from None

    if isinstance(result, Leaf):
        result = Node(syms.file_input, [result])
    return result
# okay decompiling testbed_py/test_fix.py
