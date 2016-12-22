"""Possible unit test."""

import unittest
from sys import path
path.append('..')
from src import possible
from random import randint

class PossibleTests(unittest.TestCase):
    """All possible testing methods."""

    def test_maximum_value_in_board(self):
        maximum = randint(1, 1000)
        n = range(randint(50, 100))
        board = [[randint(1, maximum) for _ in n] for _ in n]
        self.assertEqual(possible.maximum_value_in_board(board), maximum)

if __name__ == "__main__":
    unittest.main()
