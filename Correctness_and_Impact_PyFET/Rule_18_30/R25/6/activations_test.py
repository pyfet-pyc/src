def test_softmax(self):
    x = backend.placeholder(ndim=2)
    f = backend.function([x], [activations.softmax(x)])
    test_values = np.random.random((2, 5))

    result = f([test_values])[0]
    expected = _ref_softmax(test_values[0])
    self.assertAllClose(result[0], expected, rtol=1e-05)

    x = backend.placeholder(ndim=1)
    with self.assertRaises(ValueError):
        activations.softmax(x)