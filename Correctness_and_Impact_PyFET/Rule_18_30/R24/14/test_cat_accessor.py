
def test_getname_categorical_accessor(self, method):
    # GH#17509
    ser = Series([1, 2, 3], name="A").astype("category")
    expected = "A"
    result = method(ser).name
    assert result == expected