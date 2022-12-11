def test_error_tree_from_subschema(validator):
    schema = {'foo': {'schema': {'bar': {'type': 'string'}}}}
    document = {'foo': {'bar': 0}}
    assert_fail(document, schema, validator=validator)
    d_error_tree = validator.document_error_tree
    s_error_tree = validator.schema_error_tree

    assert 'foo' in d_error_tree

    assert len(d_error_tree['foo'].errors) == 1, d_error_tree['foo']
    assert d_error_tree['foo'].errors[0].code == errors.MAPPING_SCHEMA.code
    assert 'bar' in d_error_tree['foo']
    assert d_error_tree['foo']['bar'].errors[0].value == 0
    assert d_error_tree.fetch_errors_from(('foo', 'bar'))[0].value == 0

    assert 'foo' in s_error_tree
    assert 'schema' in s_error_tree['foo']
    assert 'bar' in s_error_tree['foo']['schema']
    assert 'type' in s_error_tree['foo']['schema']['bar']
    assert s_error_tree['foo']['schema']['bar']['type'].errors[0].value == 0
    assert (
        s_error_tree.fetch_errors_from(('foo', 'schema', 'bar', 'type'))[0].value == 0
    )
