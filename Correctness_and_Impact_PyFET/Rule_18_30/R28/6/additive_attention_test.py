def test_shape(self):
    # Query tensor of shape [1, 2, 4]
    q = np.array(
        [[[1.0, 1.1, 1.2, 1.3], [2.0, 2.1, 2.2, 2.3]]], dtype=np.float32
    )
    # Value tensor of shape [1, 3, 4]
    v = np.array(
        [
            [
                [1.5, 1.6, 1.7, 1.8],
                [2.5, 2.6, 2.7, 2.8],
                [3.5, 3.6, 3.7, 3.8],
            ]
        ],
        dtype=np.float32,
    )
    # Value mask tensor of shape [1, 3]
    v_mask = np.array([[True, True, False]], dtype=np.bool_)
    attention_layer = keras.layers.AdditiveAttention()
    actual = attention_layer([q, v], mask=[None, v_mask])

    expected_shape = [1, 2, 4]
    self.assertAllEqual(expected_shape, tf.shape(actual))
