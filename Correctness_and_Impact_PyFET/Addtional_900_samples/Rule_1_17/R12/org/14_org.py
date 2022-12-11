from algorithms.dfs import (
    get_factors as get, get_factors_iterative1 as get,
)

import unittest


class TestAllFactors(unittest.TestCase):
    def test_get_factors(self):
        self.assertEqual([[2, 16], [2, 2, 8], [2, 2, 2, 4], [2, 2, 2, 2, 2],
                         [2, 4, 4], [4, 8]], get_factors(32))

    def test_get_factors_iterative1(self):
        self.assertEqual([[2, 16], [4, 8], [2, 2, 8], [2, 4, 4], [2, 2, 2, 4],
                          [2, 2, 2, 2, 2]], get_factors_iterative1(32))

    def test_get_factors_iterative2(self):
        self.assertEqual([[2, 2, 2, 2, 2], [2, 2, 2, 4], [2, 2, 8], [2, 4, 4],
                          [2, 16], [4, 8]], get_factors_iterative2(32))
