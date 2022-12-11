def optimize_acq(func, m, m1, fixed, num_f):
    """Optimize acquisition function."""

    opts  = {"maxiter": 200, "maxfun": 200, "disp": False}

    T = 10
    best_value = -999
    best_theta = m1.X[0, :]

    bounds  = [(0, 1) for _ in range(m.X.shape[1] - num_f)]
    bounds = dict(bounds)
