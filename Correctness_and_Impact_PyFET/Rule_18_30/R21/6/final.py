# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 16:25:03
# Size of source mod 2**32: 988 bytes


def compute_output_shape(self, input_shape):
    input_shape = tf.TensorShape(input_shape).as_list()
    batch_rank = len(input_shape) - self.rank - 1
    try:
        if self.data_format == 'channels_last':
            return tf.TensorShape(input_shape[:batch_rank] + self._spatial_output_shape(input_shape[batch_rank:-1]) + [
             self.filters])
        return tf.TensorShape(input_shape[:batch_rank] + [
         self.filters] + self._spatial_output_shape(input_shape[batch_rank + 1:]))
    except ValueError as e:
        try:
            raise ValueError(f"One of the dimensions in the output is <= 0 due to downsampling in {self.name}. Consider increasing the input size. Received input shape {input_shape} which would produce output shape with a zero or negative value in a dimension.")
        finally:
            e = None
            del e
# okay decompiling testbed_py/test.py
