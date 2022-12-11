# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/average_pooling_test.py
# Compiled at: 2022-08-12 04:25:48
# Size of source mod 2**32: 595 bytes


def test_average_pooling_3d(self):
    pool_size = {**strides, **{str(pool.get_size()):padding(pool) for pool in layers}}
    test_utils.layer_test((keras.layers.AveragePooling3D),
      kwargs={'strides':2, 
     'padding':'valid',  'pool_size':pool_size},
      input_shape=(3, 11, 12, 10, 4))
    test_utils.layer_test((keras.layers.AveragePooling3D),
      kwargs={'strides':3, 
     'padding':'valid', 
     'data_format':'channels_first', 
     'pool_size':pool_size},
      input_shape=(3, 4, 11, 12, 10))
# okay decompiling testbed_py/average_pooling_test.py
