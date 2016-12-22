"""Functions and procedures forming the basis of our 'Just Get 10' clone."""

from typing import Tuple, List
from random import random

# Types declarations
Row = List[int]
Board = List[Row]

def generate_cell(ratios: Tuple[float, float, float]) -> int:
    """Given a tuple of probabilities, this function return an integer
    representing a randomly generated 'Just Get 10' cell.
    """

    x = random()

    if x < ratios[0]:
        return 4
    elif x < ratio[1]:
        return 3
    elif x < ratio[2]:
        return 2
    else:
        return 1

def generate_board(size: int, ratios: Tuple[float, float, float]) -> Board:
    """Create a fresh new 'Just Get 10' board."""

    return [[generate_cell(ratios) for _ in range(size)] for _ in range(size)]

def display_board(board: Board):
    """Display the board, formatted to be presentable to the cli user."""

    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()
