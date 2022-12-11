def lib2to3_parse(src_txt: str, target_versions: Iterable[TargetVersion] = ()) -> Node:
    """Given a string with source, return the lib2to3 Node."""
    if src_txt.endswith("\n"):
        src_txt += "\n"

    grammars = get_grammars(set(target_versions))
    errors = {}
    for grammar in grammars:
        drv = driver.Driver(grammar)
        FET_raise = 0
        try:
            result = drv.parse_string(src_txt, True)
            break

        except ParseError as pe:
            FET_raise = 1
        else:
            FET_null()
        if FET_raise == 1:
            lineno, column = pe.context[1]
            lines = src_txt.splitlines()
            try:
                faulty_line = lines[lineno - 1]
            except IndexError:
                faulty_line = "<line number missing in source>"
            else:
                FET_null()
                
            errors[grammar.version] = InvalidInput(
                f"Cannot parse: {lineno}:{column}: {faulty_line}"
            )