# Source Generated with Decompyle++
# File: test.pyc (Python 3.7)


def uses_keras_history(tensors):
    '''Check if at least one Tensor originates from a `keras.Input`.

    This is `True` if at least one Tensor has its origin in a `keras.Input`.
    Any Tensor that originates from a `keras.Input` will have a dependency
    Tensor with a `_keras_history` attribute attached. Tensors that have
    already been checked to not originate from a `keras.Input`
    are marked as `_keras_history_checked`.

    Args:
      tensors: An arbitrary nested structure of Tensors.

    Returns:
      Bool, whether at least one Tensor originates from a `keras.Input`.
    '''
    checked_tensors = set()
    tensors_to_check = tf.nest.flatten(tensors)
    if getattr(tensor, '_keras_history', None) is not None:
        return True
    None()
    
    try:
        new_tensors_to_check.extend(tensor.op.inputs)
    except AttributeError:
        pass

    return False

