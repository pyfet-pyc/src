def test_sync_sequential_verbose(PipenvInstance):
    with PipenvInstance() as p:
        with open(p.pipfile_path, 'w') as f:
            contents = """
[packages]
requests = "*"
        """.strip()
            f.write(contents)

        c = p.pipenv('lock')
        assert c.returncode == 0

        c = p.pipenv('sync --sequential --verbose')
        for package in p.lockfile['default']:
            assert f'Successfully installed {package}' in c.stdout
