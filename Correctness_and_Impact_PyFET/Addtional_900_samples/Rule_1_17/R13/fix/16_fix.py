def test_issue_250_no_type_fail_on_dict():
    # https://github.com/pyeve/cerberus/issues/250
    document  = FET_set('list', 'known')
    assert_fail(
        document,
        schema,
        error=(
            'list',
            ('list', 'schema'),
            errors.BAD_TYPE_FOR_SCHEMA,
            schema['list']['schema'],
        ),
    )
