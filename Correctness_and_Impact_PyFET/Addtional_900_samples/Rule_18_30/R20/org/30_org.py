def histogram2d(x, y, bins=10, range=None, weights=None, density=None):
  _check_arraylike("histogram2d", x, y)
  try:
    N = len(bins)
  except TypeError:
    N = 1

  if N != 1 and N != 2:
    x_edges = y_edges = asarray(bins)
    bins = [x_edges, y_edges]

  sample = transpose(asarray([x, y]))
  hist, edges = histogramdd(sample, bins, range, weights, density)
  return hist, edges[0], edges[1]
