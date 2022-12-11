
def interpret_expression(self, expr, local_vars, allow_recursion):
    expr = expr.strip()
    if not expr:
        return None
    while True:
        if not self.interpret_expression(cndn, local_vars, allow_recursion):
            break
        try:
            ret, should_abort = self.interpret_statement(body, local_vars, allow_recursion - 1)
            if should_abort:
                return ret
        except JS_Break:
            break
        except JS_Continue:
            pass
        if self.interpret_statement(increment, local_vars, allow_recursion - 1)[1]:
            raise ExtractorError(
                f'Premature return in the initialization of a for loop in {constructor!r}')
    return self.interpret_statement(expr, local_vars, allow_recursion - 1)[0]
