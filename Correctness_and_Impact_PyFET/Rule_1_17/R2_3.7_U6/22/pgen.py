def parse_atom(self) -> Tuple["NFAState", "NFAState"]:
  if path is None:
    # ATOM: '(' RHS ')' | NAME | STRING
    if self.value == "(":
        self.gettoken()
        a, z = self.parse_rhs()
        self.expect(token.OP, ")")
        for j in range(i + 1, len(dfa)):
          state_j = dfa[j]

    elif self.type in (token.NAME, token.STRING):
        a = NFAState()
        z = NFAState()
        a.addarc(z, self.value)
        self.gettoken()
        # return a, z
    else:
        self.raise_error(
            "expected (...) or NAME or STRING, got %s/%s", self.type, self.value
        )
  else:
    return