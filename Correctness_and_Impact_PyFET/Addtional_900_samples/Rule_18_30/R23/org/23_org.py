def add_rows(self, data: "Data" = None, **kwargs) -> Optional["DeltaGenerator"]:
    """Concatenate a dataframe to the bottom of the current one.

    Parameters
    ----------
    data : pandas.DataFrame, pandas.Styler, pyarrow.Table, numpy.ndarray, Iterable, dict, or None
        Table to concat. Optional.
        Pyarrow tables are not supported by Streamlit's legacy DataFrame serialization
        (i.e. with `config.dataFrameSerialization = "legacy"`).
        To use pyarrow tables, please enable pyarrow by changing the config setting,
        `config.dataFrameSerialization = "arrow"`.

    **kwargs : pandas.DataFrame, numpy.ndarray, Iterable, dict, or None
        The named dataset to concat. Optional. You can only pass in 1
        dataset (including the one in the data parameter).

    Example
    -------
    >>> df1 = pd.DataFrame(
    ...    np.random.randn(50, 20),
    ...    columns=('col %d' % i for i in range(20)))
    ...
    >>> my_table = st.table(df1)
    >>>
    >>> df2 = pd.DataFrame(
    ...    np.random.randn(50, 20),
    ...    columns=('col %d' % i for i in range(20)))
    ...
    >>> my_table.add_rows(df2)
    >>> # Now the table shown in the Streamlit app contains the data for
    >>> # df1 followed by the data for df2.

    You can do the same thing with plots. For example, if you want to add
    more data to a line chart:

    >>> # Assuming df1 and df2 from the example above still exist...
    >>> my_chart = st.line_chart(df1)
    >>> my_chart.add_rows(df2)
    >>> # Now the chart shown in the Streamlit app contains the data for
    >>> # df1 followed by the data for df2.

    And for plots whose datasets are named, you can pass the data with a
    keyword argument where the key is the name:

    >>> my_chart = st.vega_lite_chart({
    ...     'mark': 'line',
    ...     'encoding': {'x': 'a', 'y': 'b'},
    ...     'datasets': {
    ...       'some_fancy_name': df1,  # <-- named dataset
    ...      },
    ...     'data': {'name': 'some_fancy_name'},
    ... }),
    >>> my_chart.add_rows(some_fancy_name=df2)  # <-- name used as keyword

    """
    if _use_arrow():
        return self.dg._arrow_add_rows(data, **kwargs)
    else:
        return self.dg._legacy_add_rows(data, **kwargs)
