"""Possible unit test."""

import unittest
from sys import path
path.append('..')
from src import possible

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

if __name__ == "__main__":
    unittest.main()
