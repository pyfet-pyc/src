def test_issue_250():
    # https://github.com/pyeve/cerberus/issues/250

    document  = FET_set('list', 'is_a')
    assert_fail(
        document,
        schema,
        error=('list', ('list', 'type'), errors.BAD_TYPE, schema['list']['type']),
    )