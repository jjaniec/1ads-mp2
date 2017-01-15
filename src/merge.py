from typing import Tuple, List
from basis import generate_cell

Row = List[int]
Board = List[Row]
Coord = Tuple[int, int]

def get_similar_cells_suite(board: Board,
                            cell: Coord,
                            cells_suite: List[Coord]) -> None:
    """Put inside cell_suite all the cells that are directly or indirectly
    adjacent (excluding diagonals) to cell.
    """

    n = len(board)
    adjacent_coordinates = [ (-1, 0), (1, 0), (0, -1), (0, 1) ]

    before_cells_suite_length = len(cells_suite)
    i = 0
    while i != 4:
        x = cell[0] + adjacent_coordinates[i][0]
        y = cell[1] + adjacent_coordinates[i][1]
        if ((x >= 0 and x < n and y >= 0 and y < n) and # Are x and y inside
                                                        # board
            board[cell[1]][cell[0]] is board[y][x] and
            (x, y) not in cells_suite):
            cells_suite.append((x, y))
        i += 1
    after_cells_suite_length = len(cells_suite)

    if before_cells_suite_length is not after_cells_suite_length:
        for i in range(1, after_cells_suite_length):
            get_similar_cells_suite(board, cells_suite[i], cells_suite)

def merge_cells(board: Board, cells: List[Coord]):
    """Merge all cells located at the coordinates inside the list provided as
    paramater by incrementing the cell located a index 0 and emptying all the
    others cells (i.e. setting their value to 0).
    """

    cell_to_merge_into = cells[0]
    cells_to_empty = cells[1:]

    board[cell_to_merge_into[1]][cell_to_merge_into[0]] += 1

    i = 0
    while i < len(cells_to_empty):
        cell_to_empty = cells_to_empty[i]
        x = cell_to_empty[0]
        y = cell_to_empty[1]
        board[y][x] = 0
        i += 1

def fall_and_fill(board: Board, ratios: Tuple[float, float, float]) -> None:
    """Make cells falling when they have an empty one below them and fill these
    empty cells.
    """

    n = len(board)
    x = 0
    y = 0

    while y < n:
        while x < n:
            if board[y][x] == 0:
                fill_empty_cell(board, (x, y), ratios)
            x += 1
        x = 0
        y += 1

def fill_empty_cell(board: Board,
                    cell: Coord,
                    ratios: Tuple[float, float, float]) -> None:
    """Fill the provided empty cell."""

    x = cell[0]
    y = cell[1]
    i = 0
    while (y - i - 1) > -1:
        board[y - i][x] = board[y - i - 1][x]
        i += 1
    board[y - i][x] = generate_cell(ratios)
