def test_plugins_uninstall_non_existent(httpie_plugins, interface):
    plugin = interface.make_dummy_plugin(build=False)
    result = httpie_plugins('uninstall', plugin.name)

    assert result.exit_status == ExitStatus.ERROR
    assert (
        result.stderr.splitlines()[-1].strip()
        == f"Can't uninstall '{plugin.name}': package is not installed"
    )