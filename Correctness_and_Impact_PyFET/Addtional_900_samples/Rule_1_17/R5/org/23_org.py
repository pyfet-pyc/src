def test_private_index_mirror_lock_requirements(PipenvInstance_NoPyPI):
    # Don't use the local fake pypi
    with temp_environ(), PipenvInstance_NoPyPI(chdir=True) as p:
        # Using pypi.python.org as pipenv-test-public-package is not
        # included in the local pypi mirror
        mirror_url = os.environ.pop('PIPENV_TEST_INDEX', "https://pypi.kennethreitz.org/simple")
        # os.environ.pop('PIPENV_TEST_INDEX', None)
        with open(p.pipfile_path, 'w') as f:
            contents = """
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[[source]]
url = "https://test.pypi.org/simple"
verify_ssl = true
name = "testpypi"

[packages]
six = {version = "*", index = "testpypi"}
fake-package = "*"
            """.strip()
            f.write(contents)
        c = p.pipenv(f'install -v --pypi-mirror {mirror_url}')
        assert c.returncode == 0