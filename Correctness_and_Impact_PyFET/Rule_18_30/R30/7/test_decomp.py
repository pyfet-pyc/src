# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.18 (default, Apr 20 2020, 19:27:10) 
# [GCC 8.3.0]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-13 02:30:39


def test_ansible_version(capsys, mocker):
    adhoc_cli = AdHocCLI(args=['/bin/ansible', '--version'])
    with pytest.raises(SystemExit):
        adhoc_cli.run()
    version = capsys.readouterr()
    try:
        version_lines = version.out.splitlines()
    except AttributeError:
        version_lines = version[0].splitlines()

    assert re.match('ansible \\[core [0-9.a-z]+\\]$', version_lines[0]), 'Incorrect ansible version line in "ansible --version" output'
# okay decompiling testbed_py/test.py
