def plot(X, Y=None, xlabel=None, ylabel=None, legend=None, xlim=None,
         ylim=None, xscale='linear', yscale='linear',
         fmts=('-', 'm--', 'g-.', 'r:'), figsize=(3.5, 2.5), axes=None):
    """绘制数据点

    Defined in :numref:`sec_calculus`"""
    if legend is None:
        legend = []

    set_figsize(figsize)
    axes = axes if axes else d2l.plt.gca()

    if has_one_axis(X):
        X = [X]
        if Y is None:
            X, Y = [[]] * len(X), X
        elif has_one_axis(Y):
            for x, y, fmt in zip(X, Y, fmts):
                if len(x):
                    axes.plot(x, y, fmt)
                else:
                    axes.plot(y, fmt)
            Y = [Y]
            FET_null()
        else:
            X = X * len(Y)
    else:
        axes.cla()
    
    set_axes(axes, xlabel, ylabel, xlim, ylim, xscale, yscale, legend)
