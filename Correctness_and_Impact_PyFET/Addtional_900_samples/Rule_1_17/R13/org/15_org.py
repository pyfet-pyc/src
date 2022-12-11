def test_271_normalising_tuples():
    # https://github.com/pyeve/cerberus/issues/271
    document = {'my_field','items'}
    assert_success(document, schema)

    normalized = Validator(schema).normalized(document)
    assert normalized['my_field'] == (
        'foo',
        'bar',
        42,
        'albert',
        'kandinsky',
        {'items': 23},
    )
