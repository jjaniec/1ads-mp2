"""Possible unit test."""

import unittest
from sys import path
path.append('..')
from src import possible
from random import randint

class PossibleTests(unittest.TestCase):
    """All possible testing methods."""

    def test_is_board_still_playable(self):
        unplayable_board = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [1, 2, 3, 4]
        ]
        self.assertFalse(possible.is_board_still_playable(unplayable_board))
        playable_board = [
            [4, 1, 3, 4],
            [5, 6, 4, 9],
            [1, 2, 3, 5]
        ]
        self.assertTrue(possible.is_board_still_playable(playable_board))

    def test_maximum_value_in_board(self):
        maximum = randint(1, 1000)
        n = range(randint(50, 100))
        board = [[randint(1, maximum) for _ in n] for _ in n]
        self.assertEqual(possible.maximum_value_in_board(board), maximum)

if __name__ == "__main__":
    unittest.main()
