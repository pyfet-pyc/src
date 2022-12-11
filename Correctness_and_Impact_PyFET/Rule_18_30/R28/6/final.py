# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 06:09:48
# Size of source mod 2**32: 712 bytes


def test_shape(self):
    q = np.array([
     [
      [
       1.0, 1.1, 1.2, 1.3], [2.0, 2.1, 2.2, 2.3]]],
      dtype=(np.float32))
    v = np.array([
     [
      [
       1.5, 1.6, 1.7, 1.8],
      [
       2.5, 2.6, 2.7, 2.8],
      [
       3.5, 3.6, 3.7, 3.8]]],
      dtype=(np.float32))
    v_mask = np.array([[True, True, False]], dtype=(np.bool_))
    attention_layer = keras.layers.AdditiveAttention()
    actual = attention_layer([q, v], mask=[None, v_mask])
    expected_shape = [
     1, 2, 4]
    self.assertAllEqual(expected_shape, tf.shape(actual))
# okay decompiling testbed_py/test.py
