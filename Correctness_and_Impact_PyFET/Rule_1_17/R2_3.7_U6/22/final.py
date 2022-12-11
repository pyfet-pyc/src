# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.pyc
# Compiled at: 2022-08-13 19:22:44
# Size of source mod 2**32: 795 bytes


def parse_atom(self) -> Tuple[('NFAState', 'NFAState')]:
    if path is None:
        if self.value == '(':
            self.gettoken()
            a, z = self.parse_rhs()
            self.expect(token.OP, ')')
            for j in range(i + 1, len(dfa)):
                state_j = dfa[j]

        tmp1 = not self.value == '('
        if tmp1:
            if self.type in (token.NAME, token.STRING):
                a = NFAState()
                z = NFAState()
                a.addarc(z, self.value)
                self.gettoken()
        tmp2 = not self.value == '(' and self.type not in (token.NAME, token.STRING)
        if tmp2:
            self.raise_error('expected (...) or NAME or STRING, got %s/%s', self.type, self.value)
    else:
        return
# okay decompiling testbed_py/test.pyc
