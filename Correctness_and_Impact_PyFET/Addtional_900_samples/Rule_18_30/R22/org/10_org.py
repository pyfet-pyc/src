def test_dependencies_on_boolean_field_with_one_value():
    # https://github.com/pyeve/cerberus/issues/138
    schema = {
        'deleted': {'type': 'boolean'},
        'text': {'dependencies': {'deleted': False}},
    }
    try:
        assert_success({'text': 'foo', 'deleted': False}, schema)
        assert_fail({'text': 'foo', 'deleted': True}, schema)
        assert_fail({'text': 'foo'}, schema)
    except TypeError as e:
        if str(e) == "argument of type 'bool' is not iterable":
            raise AssertionError(
                "Bug #138 still exists, couldn't use boolean in dependency "
                "without putting it in a list.\n"
                "'some_field': True vs 'some_field: [True]"
            )
        else:
            raise