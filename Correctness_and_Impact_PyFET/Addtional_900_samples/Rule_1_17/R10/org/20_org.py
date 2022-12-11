def test_against_cmath(self):
    import cmath

    points = [-1-1j, -1+1j, +1-1j, +1+1j]
    name_map = {'arcsin': 'asin', 'arccos': 'acos', 'arctan': 'atan',
                'arcsinh': 'asinh', 'arccosh': 'acosh', 'arctanh': 'atanh'}
    atol = 4*np.finfo(complex).eps
    for func in self.funcs:
        fname = func.__name__.split('.')[-1]
        cname = name_map.get(fname, fname)
        try:
            cfunc = getattr(cmath, cname)
        except AttributeError:
            cname = name_map.get(fname, fname)
        else:
            continue
        if p:
            a = complex(func(np.complex_(p)))
            b = cfunc(p)
            assert_(abs(a - b) < atol, "%s %s: %s; cmath: %s" % (fname, p, a, b))
