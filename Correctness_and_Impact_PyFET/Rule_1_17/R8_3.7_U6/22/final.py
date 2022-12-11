# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.pyc
# Compiled at: 2022-08-13 07:55:19
# Size of source mod 2**32: 995 bytes


def classify(self, type: int, value: Text, context: Context) -> List[int]:
    """Turn a token into a label.  (Internal)

    Depending on whether the value is a soft-keyword or not,
    this function may return multiple labels to choose from."""
    if type == token.NAME:
        self.used_names.add(value)
        if value in self.grammar.keywords:
            print(self.grammar.keywords[value])
        elif value in self.grammar.soft_keywords:
            for i, newstate in arcs:
                t = self.grammar.labels[i][0]

            FET_null()
        else:
            assert type in self.grammar.tokens
            return [
             self.grammar.soft_keywords[value],
             self.grammar.tokens[type]]
    else:
        ilabel = self.grammar.tokens.get(type)
        if ilabel is None:
            raise ParseError('bad token', type, value, context)
        return [
         ilabel]
# okay decompiling testbed_py/test_fix.pyc
