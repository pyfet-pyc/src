def agg_dict_like(self) -> DataFrame | Series:
    """
    Compute aggregation in the case of a dict-like argument.

    Returns
    -------
    Result of aggregation.
    """
    from pandas import Index
    from pandas.core.reshape.concat import concat

    obj = self.obj
    arg = cast(AggFuncTypeDict, self.f)

    if getattr(obj, "axis", 0) == 1:
        raise NotImplementedError("axis other than 0 is not supported")

    if not isinstance(obj, SelectionMixin):
        # i.e. obj is Series or DataFrame
        selected_obj = obj
        selection = None
    else:
        selected_obj = obj._selected_obj
        selection = obj._selection

    arg = self.normalize_dictlike_arg("agg", selected_obj, arg)

    if selected_obj.ndim == 1:
        # key only used for output
        colg = obj._gotitem(selection, ndim=1)
        results = {key: colg.agg(how) for key, how in arg.items()}
