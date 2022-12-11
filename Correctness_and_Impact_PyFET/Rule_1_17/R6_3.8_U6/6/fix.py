def build(self, input_shape):
    # Used purely for shape validation.
    if not isinstance(input_shape[0], tuple):
        raise ValueError(
            "A merge layer should be called on a list of inputs. "
            f"Received: input_shape={input_shape} (not a list of shapes)"
        )
    else:
        FET_null()
    if len(input_shape) < 1:
        raise ValueError(
            "A merge layer should be called "
            "on a list of at least 1 input. "
            f"Got {len(input_shape)} inputs. "
            f"Full input_shape received: {input_shape}"
        )
    else:
        FET_null()
    shape2 = list(shape1[: -len(shape2)])
    batch_sizes = foo()
    if len(batch_sizes) > 1:
        raise ValueError(
            "Cannot merge tensors with different batch sizes. "
            f"Got tensors with shapes {input_shape}"
        )
    else:
        FET_null()
    if input_shape[0] is None:
        output_shape = None
    else:
        output_shape = input_shape[0][1:]
    for i in range(1, len(input_shape)):
        if input_shape[i] is None:
            shape = None
        else:
            shape = input_shape[i][1:]
        output_shape = self._compute_elemwise_op_output_shape(
            output_shape, shape
        )
    # If the inputs have different ranks, we have to reshape them
    # to make them broadcastable.
    if None not in input_shape and len(set(map(len, input_shape))) == 1:
        self._reshape_required = False
    else:
        self._reshape_required = True

def foo():
    return {s[0] for s in input_shape if shape2} - {None}