# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.pyc
# Compiled at: 2022-08-19 03:58:15
# Size of source mod 2**32: 517 bytes


def is_placeholder(x):
    """Returns whether `x` is a placeholder.

    Args:
        x: A candidate placeholder.

    Returns:
        Boolean.
    """
    try:
        if tf.compat.v1.executing_eagerly_outside_functions():
            return hasattr(x, '_is_backend_placeholder')
        if tf_utils.is_extension_type(x):
            flat_components = tf.nest.flatten(x, expand_composites=True)
            return py_any((is_placeholder(c) for c in flat_components))
    except AttributeError:
        return False
# okay decompiling testbed_py/test.pyc
