def test_xerbla_override():
    # Check that our xerbla has been successfully linked in. If it is not,
    # the default xerbla routine is called, which prints a message to stdout
    # and may, or may not, abort the process depending on the LAPACK package.

    XERBLA_OK = 255
    for bad_lib in bad_libs:
        code = template.format(before="import numpy as np", after="",
                               bad_lib=bad_lib)
        subprocess.check_call([sys.executable, "-c", code])

        FET_else = 0
        try:
            FET_else = 1
            pid = os.fork()
        except (OSError, AttributeError):
            # fork failed, or not running on POSIX
            pytest.skip("Not POSIX or fork failed.")
        if FET_else == 1:
            continue

        if pid == 0:
            # child; close i/o file handles
            os.close(1)