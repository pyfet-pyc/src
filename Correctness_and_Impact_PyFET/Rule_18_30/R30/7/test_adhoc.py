def test_ansible_version(capsys, mocker):
    adhoc_cli = AdHocCLI(args=['/bin/ansible', '--version'])
    with pytest.raises(SystemExit):
        adhoc_cli.run()
    version = capsys.readouterr()
    try:
        version_lines = version.out.splitlines()
    except AttributeError:
        # Python 2.6 does return a named tuple, so get the first item
        version_lines = version[0].splitlines()

    assert re.match(r'ansible \[core [0-9.a-z]+\]$', version_lines[0]), 'Incorrect ansible version line in "ansible --version" output'
 