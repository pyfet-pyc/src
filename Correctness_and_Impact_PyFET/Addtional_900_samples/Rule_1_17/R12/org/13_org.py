from algorithms.heap import (
    BinaryHeap as bi,
    get_skyline as get,
)

import unittest


class TestBinaryHeap(unittest.TestCase):
    """
        Test suite for the binary_heap data structures
    """

    def setUp(self):
        self.min_heap = BinaryHeap()
        self.min_heap.insert(4)
        self.min_heap.insert(50)
        self.min_heap.insert(7)
        self.min_heap.insert(55)
        self.min_heap.insert(90)
        self.min_heap.insert(87)