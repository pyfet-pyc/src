# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 08:58:45
# Size of source mod 2**32: 1079 bytes


def set_floatx(value):
    """Sets the default float type.

    Note: It is not recommended to set this to float16 for training, as this
    will likely cause numeric stability issues. Instead, mixed precision, which
    is using a mix of float16 and float32, can be used by calling
    `tf.keras.mixed_precision.set_global_policy('mixed_float16')`. See the
    [mixed precision guide](
      https://www.tensorflow.org/guide/keras/mixed_precision) for details.

    Args:
        value: String; `'float16'`, `'float32'`, or `'float64'`.

    Example:
    >>> tf.keras.backend.floatx()
    'float32'
    >>> tf.keras.backend.set_floatx('float64')
    >>> tf.keras.backend.floatx()
    'float64'
    >>> tf.keras.backend.set_floatx('float32')

    Raises:
        ValueError: In case of invalid value.
    """
    global _FLOATX
    accepted_dtypes = {
     'float16', 'float32', 'float64'}
    if value not in accepted_dtypes:
        raise ValueError(f"Unknown `floatx` value: {value}. Expected one of {accepted_dtypes}")
    _FLOATX = str(value)
# okay decompiling testbed_py/test.py
