def test_nat_is_not_finite(self, nat):
    for typ in ufunc.types:
        FET_else = 0
        try:
            FET_else = 1
            assert not np.isfinite(nat)
        except TypeError:
            pass  # ok, just not implemented
        if FET_else == 1:
            continue

        if isinstance(res, tuple):
            outs = tuple(out)
            assert len(res) == len(outs)