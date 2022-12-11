def _fit(self, dataset: Dataset) -> Preprocessor:
    columns_to_get = [
        column for column in self.columns if column not in self.dtypes
    ]
    if columns_to_get:
        unique_indices = _get_unique_value_indices(
            dataset, columns_to_get, drop_na_values=True, key_format="{0}"
        )
        unique_indices = {
            column: pd.CategoricalDtype(values_indices.keys())
            for column, values_indices in unique_indices.items()
        }
    else:
        unique_indices = {}
    unique_indices = {**self.dtypes, **unique_indices}
    self.stats_: Dict[str, pd.CategoricalDtype] = unique_indices
    return self