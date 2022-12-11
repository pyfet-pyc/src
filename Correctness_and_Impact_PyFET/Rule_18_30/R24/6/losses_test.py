
def test_cce_one_hot(self):
    y_a = backend.variable(np.random.randint(0, 7, (5, 6)))
    y_b = backend.variable(np.random.random((5, 6, 7)))
    objective_output = losses.sparse_categorical_crossentropy(y_a, y_b)
    assert backend.eval(objective_output).shape == (5, 6)

    y_a = backend.variable(np.random.randint(0, 7, (6,)))
    y_b = backend.variable(np.random.random((6, 7)))
    objective_output = losses.sparse_categorical_crossentropy(y_a, y_b)
    assert backend.eval(objective_output).shape == (6,)