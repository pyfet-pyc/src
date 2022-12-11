# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 02:30:04
# Size of source mod 2**32: 2571 bytes


def placeholder(shape=None, ndim=None, dtype=None, sparse=False, name=None, ragged=False):
    """Instantiates a placeholder tensor and returns it.

    Args:
        shape: Shape of the placeholder
            (integer tuple, may include `None` entries).
        ndim: Number of axes of the tensor.
            At least one of {`shape`, `ndim`} must be specified.
            If both are specified, `shape` is used.
        dtype: Placeholder type.
        sparse: Boolean, whether the placeholder should have a sparse type.
        name: Optional name string for the placeholder.
        ragged: Boolean, whether the placeholder should have a ragged type.
            In this case, values of 'None' in the 'shape' argument represent
            ragged dimensions. For more information about RaggedTensors, see
            this [guide](https://www.tensorflow.org/guide/ragged_tensor).

    Raises:
        ValueError: If called with sparse = True and ragged = True.

    Returns:
        Tensor instance (with Keras metadata included).

    Examples:

    >>> input_ph = tf.keras.backend.placeholder(shape=(2, 4, 5))
    >>> input_ph
    <KerasTensor: shape=(2, 4, 5) dtype=float32 (created by layer ...)>

    """
    if sparse:
        if ragged:
            raise ValueError('Cannot set both sparse and ragged to True when creating a placeholder.')
    elif dtype is None:
        dtype = floatx()
    else:
        if not shape:
            if ndim:
                shape = (None, ) * ndim
        if tf.compat.v1.executing_eagerly_outside_functions():
            if sparse:
                spec = tf.SparseTensorSpec(shape=shape, dtype=dtype)
            else:
                if ragged:
                    ragged_rank = 0
                    for i in range(1, len(shape)):
                        if not shape[i] is None:
                            if not hasattr(shape[i], 'value') or shape[i].value is None:
                                ragged_rank = i

            if a:
                spec = tf.TensorSpec(shape=shape, dtype=dtype, name=name)
        else:
            flat_components = tf.nest.flatten(x, expand_composites=True)
    if tf.executing_eagerly():
        from keras.engine import input_layer
        x = input_layer.Input(tensor=x)
        x._is_backend_placeholder = True
# okay decompiling test.pyc
