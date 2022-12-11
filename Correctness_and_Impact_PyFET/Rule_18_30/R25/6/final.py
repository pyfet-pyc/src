# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/activations_test.py
# Compiled at: 2022-08-12 02:29:15
# Size of source mod 2**32: 401 bytes


def test_softmax(self):
    x = backend.placeholder(ndim=2)
    f = backend.function([x], [activations.softmax(x)])
    test_values = np.random.random((2, 5))
    result = f([test_values])[0]
    expected = _ref_softmax(test_values[0])
    self.assertAllClose((result[0]), expected, rtol=1e-05)
    x = backend.placeholder(ndim=1)
    with self.assertRaises(ValueError):
        activations.softmax(x)
# okay decompiling testbed_py/activations_test.py
