def get_tokens_unprocessed(self, text, stack=('root',)):
    """
    Split ``text`` into (tokentype, text) pairs.

    ``stack`` is the initial stack (default: ``['root']``)
    """
    pos = 0
    tokendefs = self._tokens
    statestack = list(stack)
    statetokens = tokendefs[statestack[-1]]
    while 1:
        for rexmatch, action, new_state in statetokens:
            m = rexmatch(text, pos)
            if m:
                if action is not None:
                    if type(action) is _TokenType:
                        yield from action(self, m)
                pos = m.end()