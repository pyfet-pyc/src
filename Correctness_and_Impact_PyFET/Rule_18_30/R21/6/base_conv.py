def compute_output_shape(self, input_shape):
    input_shape = tf.TensorShape(input_shape).as_list()
    batch_rank = len(input_shape) - self.rank - 1
    try:
        if self.data_format == "channels_last":
            return tf.TensorShape(
                input_shape[:batch_rank]
                + self._spatial_output_shape(input_shape[batch_rank:-1])
                + [self.filters]
            )
        # else:
        return tf.TensorShape(
            input_shape[:batch_rank]
            + [self.filters]
            + self._spatial_output_shape(input_shape[batch_rank + 1 :])
        )

    except ValueError as e:
        raise ValueError(
            f"One of the dimensions in the output is <= 0 "
            f"due to downsampling in {self.name}. Consider "
            f"increasing the input size. "
            f"Received input shape {input_shape} which would produce "
            f"output shape with a zero or negative value in a "
            f"dimension."
        )