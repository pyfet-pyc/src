def test_nat_is_not_finite(self, nat):
    for typ in ufunc.types:
        try:
            assert not np.isfinite(nat)
        except TypeError:
            pass  # ok, just not implemented
        else:
            continue

        if isinstance(res, tuple):
            outs = tuple(out)
            assert len(res) == len(outs)