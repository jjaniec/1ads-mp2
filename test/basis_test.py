"""Basis unit test."""

import unittest
from sys import path
path.append('..')
from src import basis

class BasisTests(unittest.TestCase):
    """All basis testing methods."""

    def test_generate_cell(self):
        ratios_one = (0.0, 0.0, 0.0)
        self.assertEqual(basis.generate_cell(ratios_one), 1)
        ratios_two = (0.0, 0.0, 1.0)
        self.assertEqual(basis.generate_cell(ratios_two), 2)
        ratios_three = (0.0, 1.0, 1.0)
        self.assertEqual(basis.generate_cell(ratios_three), 3)
        ratios_four = (1.0, 1.0, 1.0)
        self.assertEqual(basis.generate_cell(ratios_four), 4)

    def test_generate_board(self):
        ratios_three = (0.0, 1.0, 1.0)
        n = 2
        board_three = [ [3, 3], [3, 3] ]
        self.assertEqual(basis.generate_board(n, ratios_three), board_three)

        ratios_one = (0.0, 0.0, 0.0)
        n = 5
        board_one = [ 
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]
        ]
        self.assertEqual(basis.generate_board(n, ratios_one), board_one)

if __name__ == "__main__":
    unittest.main()
