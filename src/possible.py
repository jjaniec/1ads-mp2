"""All functions concerning the computation of the moves avalaible to the
player.
"""

from typing import List, Any

# Type aliases
Row = List[int]
Board = List[Row]

def maximum_value_in_board(board: Board) -> int:
    """Given a board, it returns the maximum value in it."""

    return max(flatten(board))

def flatten(l: List[List[Any]]) -> List[Any]:
    """Return a one dimensional list made from a two dimensional list."""

    return [x for y in l for x in y]
