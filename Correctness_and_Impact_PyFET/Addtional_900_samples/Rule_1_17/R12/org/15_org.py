from algorithms.bfs import (
    count_islands as co,
    maze_search as maz,
    ladder_length as la,
)

import unittest


class TestCountIslands(unittest.TestCase):

    def test_count_islands(self):
        grid_1 = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0]]
        self.assertEqual(1, count_islands(grid_1))
        grid_2 = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0],
                  [0, 0, 0, 1, 1]]
        self.assertEqual(3, count_islands(grid_2))
        grid_3 = [[1, 1, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1],
                  [0, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 0]]
        self.assertEqual(3, count_islands(grid_3))
        grid_4 = [[1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1],
                  [1, 1, 1, 1, 0, 0]]
        self.assertEqual(5, count_islands(grid_4))
