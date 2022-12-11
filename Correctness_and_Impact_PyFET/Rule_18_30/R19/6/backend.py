def is_placeholder(x):
    """Returns whether `x` is a placeholder.

    Args:
        x: A candidate placeholder.

    Returns:
        Boolean.
    """
    try:
        if tf.compat.v1.executing_eagerly_outside_functions():
            return hasattr(x, "_is_backend_placeholder")

        if tf_utils.is_extension_type(x):
            flat_components = tf.nest.flatten(x, expand_composites=True)
            return py_any(is_placeholder(c) for c in flat_components)

    except AttributeError:
        return False