def http_response_type(lexer, match, ctx):
    status_match = RE_STATUS_LINE.match(match.group())
    if status_match is None:
        return None

    status_code, text, reason = status_match.groups()
    status_type = precise(
        lexer,
        STATUS_TYPES.get(status_code[0]),
        pygments.token.Number
    )

    groups = pygments.lexer.bygroups(
        status_type,
        pygments.token.Text,
        status_type
    )
    yield from groups(lexer, status_match, ctx)

