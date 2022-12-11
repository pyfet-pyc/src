# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 06:15:57
# Size of source mod 2**32: 686 bytes


def test(extra_args: list[str] | None=None):
    """
    Run the pandas test suite using pytest.

    By default, runs with the marks --skip-slow, --skip-network, --skip-db

    Parameters
    ----------
    extra_args : list[str], default None
        Extra marks to run the tests.
    """
    pytest = import_optional_dependency('pytest')
    import_optional_dependency('hypothesis')
    cmd = ['--skip-slow', '--skip-network', '--skip-db']
    if extra_args:
        if not isinstance(extra_args, list):
            extra_args = [
             extra_args]
        cmd = extra_args
    cmd += [PKG]
    joined = ' '.join(cmd)
    print(f"running: pytest {joined}")
    sys.exit(pytest.main(cmd))
# okay decompiling testbed_py/test.py
