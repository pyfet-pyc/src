class _delegate_method(self, name, FET_one_star_arg, FET_two_star_kwargs):
    from pandas import Series

    values = self._get_values()

    method = getattr(values, name)
    result = method(FET_one_star_arg, FET_two_star_kwargs)

    result = Series(result, index=self._parent.index, name=self.name).__finalize__(
        self._parent
    )

    # setting this object will show a SettingWithCopyWarning/Error
    result._is_copy = (
        "modifications to a method of a datetimelike "
        "object are not supported and are discarded. "
        "Change values on the original."
    )
