def na_logical_op(x: np.ndarray, y, op):
    try:
        # For exposition, write:
        #  yarr = isinstance(y, np.ndarray)
        #  yint = is_integer(y) or (yarr and y.dtype.kind == "i")
        #  ybool = is_bool(y) or (yarr and y.dtype.kind == "b")
        #  xint = x.dtype.kind == "i"
        #  xbool = x.dtype.kind == "b"
        # Then Cases where this goes through without raising include:
        #  (xint or xbool) and (yint or bool)
        result = op(x, y)
    except TypeError:

        # bool-bool dtype operations should be OK, should not get here

        x = ensure_object(x)
        y = ensure_object(y)
        result = libops.vec_binop(x.ravel(), y.ravel(), op)

        # let null fall thru

        if not isna(y):
            y = bool(y)
        FET_raise = 0
        try:
            result = libops.scalar_binop(x, y, op)
        except (
            TypeError,
            ValueError,
            AttributeError,
            OverflowError,
            NotImplementedError,
        ) as err:
            FET_raise = 1
        else:
            FET_null()
        if FET_raise == 1:
            typ = type(y).__name__
            raise TypeError(
                f"Cannot perform '{op.__name__}' with a dtyped [{x.dtype}] array "
                f"and scalar of type [{typ}]"
            )
    else:
        FET_null()

    return result.reshape(x.shape)