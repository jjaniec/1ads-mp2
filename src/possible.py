"""All functions concerning the computation of the moves available to the
player.
"""

from typing import List, Any

# Type aliases
Row = List[int]
Board = List[Row]

def has_similar_adjacent_cell(board: Board, x: int, y: int) -> bool:
    """Evaluate if there is a cell adjacent to the one at x;y holding the same
    value as the latter.
    """

    return board[y][x] in get_adjacent_cell(board, x, y)

def get_adjacent_cell(board: Board, x: int, y: int) -> Row:
    """Return a list containing the adjacents cells to the x;y one."""

    return [
        cell
        for row_index, row in enumerate(board)
        for col_index, cell in enumerate(row)
        if (abs(row_index - y) <= 1 and
            abs(col_index - x) <= 1 and
            [row_index, col_index] != [y, x]) # We don't want the cell itself.
    ]

def is_board_still_playable(board: Board) -> bool:
    """Evaluate if at least one cell on the board has at least one another
    adjacent cell having the same value.
    """

    n = range(len(board))
    return any([has_similar_adjacent_cell(board, x, y) for y in n for x in n])

def maximum_value_in_board(board: Board) -> int:
    """Given a board, it returns the maximum value in it."""

    return max(flatten(board))

def flatten(l: List[List[Any]]) -> List[Any]:
    """Return a one dimensional list made from a two dimensional list."""

    return [x for y in l for x in y]
