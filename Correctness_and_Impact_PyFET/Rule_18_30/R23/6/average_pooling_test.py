
def test_average_pooling_3d(self):
    pool_size = {**strides, **{padding(pool):str(pool.get_size()) for pool in layers}}
    test_utils.layer_test(
        keras.layers.AveragePooling3D,
        kwargs={"strides": 2, "padding": "valid", "pool_size": pool_size},
        input_shape=(3, 11, 12, 10, 4),
    )
    
    test_utils.layer_test(
        keras.layers.AveragePooling3D,
        kwargs={
            "strides": 3,
            "padding": "valid",
            "data_format": "channels_first",
            "pool_size": pool_size,
        },
        input_shape=(3, 4, 11, 12, 10),
    )

