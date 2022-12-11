def refuse_with_confirmation(proc, TIMEOUT):
    """Ensures that fix can be refused when confirmation enabled."""
    _set_confirmation(proc, True)

    proc.sendline(u'ehco test')

    proc.sendline(u'fuck')
    assert proc.expect([TIMEOUT, u'echo test'])
    assert proc.expect([TIMEOUT, u'enter'])
    assert proc.expect_exact([TIMEOUT, u'ctrl+c'])
    proc.send('\003')

    assert proc.expect([TIMEOUT, u'Aborted'])

