def f(*inps, **kwargs):
    *args, inp = inps
    inp = np.array(inp)
    shape = inp.shape

    if len(shape) == len(input_shape):
      out_shape = output_shape
    else:
      out_shape = (shape[0],) + output_shape

    # Add empty dimension if inputs is not a list
    if len(shape) == len(input_shape):
      inp.shape = (1, ) + inp.shape

    result = np.asarray([function(*args, i) for i in inp])
    result.shape = out_shape
    return result(self, inp, shape, *inps, **kwargs)

