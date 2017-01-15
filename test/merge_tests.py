"""Merge unit test."""

import unittest
from sys import path
path.append('../src')
import merge
from random import randint

class MergeTests(unittest.TestCase):
    """All merge testing methods."""

    def test_get_similar_cells_suite(self):
        board = [
            [ 2, 3, 2, 4, 2 ],
            [ 2, 2, 2, 5, 2 ],
            [ 1, 1, 2, 3, 1 ],
            [ 2, 2, 2, 2, 2 ],
            [ 4, 1, 3, 1, 1 ]
        ]
        origin_cell = (2, 1)
        cell_suite = [ origin_cell ]
        cell_suite_resolved_sorted = [
            (0, 0),
            (2, 0),
            (0, 1),
            (1, 1),
            (2, 1),
            (2, 2),
            (0, 3),
            (1, 3),
            (2, 3),
            (3, 3),
            (4, 3)
        ]

        merge.get_similar_cells_suite(board, origin_cell, cell_suite)
        cell_suite_sorted = sorted(cell_suite, key=lambda v: (v[1], v[0]))

        self.assertEqual(cell_suite[0], origin_cell)
        self.assertEqual(cell_suite_sorted, cell_suite_resolved_sorted)

    def test_merge_cells(self):
        board = [
            [ 1, 1, 1, 2 ],
            [ 2, 1, 3, 1 ],
            [ 1, 1, 4, 1 ],
            [ 3, 1, 1, 2 ]
        ]
        board_resolved = [
            [ 0, 0, 0, 2 ],
            [ 2, 0, 3, 1 ],
            [ 0, 2, 4, 1 ],
            [ 3, 0, 0, 2 ]
        ]
        cells_to_merge = [
            (1, 2),
            (0, 0),
            (1, 0),
            (2, 0),
            (1, 1),
            (0, 2),
            (1, 3),
            (2, 3)
        ]

        merge.merge_cells(board, cells_to_merge)
        self.assertEqual(board, board_resolved)

    def test_fall_and_fill(self):
        board = [
            [ 0, 0, 1, 1 ],
            [ 0, 5, 2, 2 ],
            [ 0, 0, 0, 3 ],
            [ 0, 0, 0, 0 ]
        ]
        board_resolved = [
            [ 4, 4, 4, 4 ],
            [ 4, 4, 4, 1 ],
            [ 4, 4, 1, 2 ],
            [ 4, 5, 2, 3 ]
        ]

        merge.fall_and_fill(board, (1.0, 1.0, 1.0))
        self.assertEqual(board, board_resolved)

if __name__ == "__main__":
    unittest.main()
