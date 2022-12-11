def test_cat_accessor_api(self):
    # GH#9322

    if Series.cat is CategoricalAccessor:
        ser = Series(list("aabbcde")).astype("category")

    invalid = Series([1])