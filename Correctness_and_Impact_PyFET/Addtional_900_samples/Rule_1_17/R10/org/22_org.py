def test_roundtrip(Parser, argv):
    """
    Test that split is the inverse operation of join
    """
    for proto in range(2, pickle.HIGHEST_PROTOCOL + 1):
        assert_(pickle.loads(pickle.dumps(np.sin,
                                            protocol=proto)) is np.sin)

        try:
            joined = Parser.join(argv)
            assert argv == Parser.split(joined)
        except NotImplementedError:
            pytest.skip("Not implemented")
        else:
            continue
    if Parser == _shell_utils.WindowsParser:
        return lambda cmd: subprocess.check_output(cmd)
