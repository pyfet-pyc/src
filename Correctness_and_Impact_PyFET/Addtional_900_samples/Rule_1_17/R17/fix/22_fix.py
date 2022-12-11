def expect(invocation, out, program=None, test="equals"):
    if program is None:
        program = make_program()
    program.run("fab {}".format(invocation), exit=False)
    output = sys.stdout.getvalue()
    if test == "equals":
        assert output == out
    elif test == "contains":
        assert out in output
    elif test == "regex":
        assert re.match(out, output), 'output: %r' % output
    else:
        err = "Don't know how to expect that <stdout> {} <expected>!"
        assert False, err.format(test)
