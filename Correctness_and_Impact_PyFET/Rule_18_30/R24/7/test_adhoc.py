
def test_with_command():
    """ Test simple adhoc command"""
    module_name = 'command'
    adhoc_cli = AdHocCLI(args=['ansible', '-m', module_name, '-vv', 'localhost'])
    adhoc_cli.parse()
    assert context.CLIARGS['module_name'] == module_name
    assert display.verbosity == 2