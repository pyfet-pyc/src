
def array_ufunc(self, ufunc: np.ufunc, method: str, *inputs: Any, **kwargs: Any):
    """
    Compatibility with numpy ufuncs.

    See also
    --------
    numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_ufunc__
    """
    from pandas.core.generic import NDFrame
    from pandas.core.internals import BlockManager

    cls = type(self)

    kwargs = _standardize_out_kwarg(**kwargs)

    # for backwards compatibility check and potentially fallback for non-aligned frames
    result = _maybe_fallback(ufunc, method, *inputs, **kwargs)
    if result is not NotImplemented:
        return result

    # for binary ops, use our custom dunder methods
    result = maybe_dispatch_ufunc_to_dunder_op(self, ufunc, method, *inputs, **kwargs)
    if result is not NotImplemented:
        return result

    # Determine if we should defer.
    no_defer = (
        np.ndarray.__array_ufunc__,
        cls.__array_ufunc__,
    )

    for item in inputs:
        higher_priority = (
            hasattr(item, "__array_priority__")
            and item.__array_priority__ > self.__array_priority__
        )
        has_array_ufunc = (
            hasattr(item, "__array_ufunc__")
            and type(item).__array_ufunc__ not in no_defer
            and not isinstance(item, self._HANDLED_TYPES)
        )
        if higher_priority or has_array_ufunc:
            return NotImplemented

        # align all the inputs.
        types = tuple(type(x) for x in inputs)
        alignable = [x for x, t in zip(inputs, types) if issubclass(t, NDFrame)]

        if len(alignable) > 1:
            # This triggers alignment.
            # At the moment, there aren't any ufuncs with more than two inputs
            # so this ends up just being x1.index | x2.index, but we write
            # it to handle *args.

            if len(set(types)) > 1:
                # We currently don't handle ufunc(DataFrame, Series)
                # well. Previously this raised an internal ValueError. We might
                # support it someday, so raise a NotImplementedError.
                raise NotImplementedError(
                    "Cannot apply ufunc {} to mixed DataFrame and Series "
                    "inputs.".format(ufunc)
                )
            axes = self.axes