# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/losses_test.py
# Compiled at: 2022-08-11 22:17:16
# Size of source mod 2**32: 514 bytes


def test_cce_one_hot(self):
    y_a = backend.variable(np.random.randint(0, 7, (5, 6)))
    y_b = backend.variable(np.random.random((5, 6, 7)))
    objective_output = losses.sparse_categorical_crossentropy(y_a, y_b)
    assert backend.eval(objective_output).shape == (5, 6)
    y_a = backend.variable(np.random.randint(0, 7, (6, )))
    y_b = backend.variable(np.random.random((6, 7)))
    objective_output = losses.sparse_categorical_crossentropy(y_a, y_b)
    assert backend.eval(objective_output).shape == (6, )
# okay decompiling testbed_py/losses_test.py
