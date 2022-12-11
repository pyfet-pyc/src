if __name__ == "__main__":
    # Run tests, including shrinking and reporting any known failures.
    test_idempotent_any_syntatically_valid_python()

    # If Atheris is available, run coverage-guided fuzzing.
    # (if you want only bounded fuzzing, just use `pytest fuzz.py`)
    try:
        import sys

        import atheris
    except ImportError:
        pass
    else:
        test = test_idempotent_any_syntatically_valid_python
        atheris.Setup(sys.argv, test.hypothesis.fuzz_one_input)
        atheris.Fuzz()
