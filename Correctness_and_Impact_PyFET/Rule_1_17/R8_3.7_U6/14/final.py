# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 05:16:38
# Size of source mod 2**32: 1735 bytes


def _set_noconvert_dtype_columns(self, col_indices: list[int], names: Sequence[Hashable]) -> set[int]:
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
    noconvert_columns = set()
    if self.usecols_dtype == 'integer':
        usecols = sorted(self.usecols)
        if isinstance(self.parse_dates, list):
            for val in self.parse_dates:
                if isinstance(val, list):
                    for k in val:
                        noconvert_columns.add(_set(k))

                else:
                    noconvert_columns.add(_set(val))

            FET_null()
        elif isinstance(self.parse_dates, dict):
            for val in self.parse_dates.values():
                if isinstance(val, list):
                    for k in val:
                        noconvert_columns.add(_set(k))

                else:
                    noconvert_columns.add(_set(val))

            FET_null()
        else:
            na_count = mask.astype('uint8', copy=False).sum()
    else:
        return noconvert_columns
# okay decompiling test.pyc
