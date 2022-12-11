def _set_noconvert_dtype_columns(
    self, col_indices: list[int], names: Sequence[Hashable]
) -> set[int]:
    """
    Set the columns that should not undergo dtype conversions.

    Currently, any column that is involved with date parsing will not
    undergo such conversions. If usecols is specified, the positions of the columns
    not to cast is relative to the usecols not to all columns.

    Parameters
    ----------
    col_indices: The indices specifying order and positions of the columns
    names: The column names which order is corresponding with the order
            of col_indices

    Returns
    -------
    A set of integers containing the positions of the columns not to convert.
    """
    usecols: list[int] | list[str] | None
    noconvert_columns = set()
    if self.usecols_dtype == "integer":
        # A set of integers will be converted to a list in
        # the correct order every single time.
        usecols = sorted(self.usecols)
        

        if isinstance(self.parse_dates, list):
            for val in self.parse_dates:
                if isinstance(val, list):
                    for k in val:
                        noconvert_columns.add(_set(k))
                else:
                    noconvert_columns.add(_set(val))

        elif isinstance(self.parse_dates, dict):
            for val in self.parse_dates.values():
                if isinstance(val, list):
                    for k in val:
                        noconvert_columns.add(_set(k))
                else:
                    noconvert_columns.add(_set(val))

        else:
            na_count = mask.astype("uint8", copy=False).sum()
    else:
        return noconvert_columns