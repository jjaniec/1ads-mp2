import sys
from typing import Tuple, List, intArray, TupleArray
from basis import *

#3.3[0]
def     get_appendable_in_arr(arr: Board, coords: Tuple[int, int], coordstoadd: Tuple[int, int]) -> int:
    """Tell if an element in Board should be added in the TupleArray returned by
    get_adj_cells function"""

    if (arr[coords[0]][coords[1]] == arr[coordstoadd[0]][coordstoadd[1]]):
        return (0);
    return (1);

def     get_adj_cells(n: int, arr: Board, coords: Tuple[int, int], li: TupleArray) -> void:
    """Return an array of tuple of adjacent cells content equal of the given one"""
    coordstocheck = [(-1, 0), (1, 0), (0, -1), (0, 1)];
    i = 0;

    while (i != 4):
        x = coords[1] + coordstocheck[i][1];
        y = coords[0] + coordstocheck[i][0];
        if (x >= 0 and x < n and y >= 0 and y < n):
            if (get_appendable_in_arr(arr, coords, (y, x)) == 0):
                li.append((y, x));
        i += 1;
#3.3[1]
def     change_cells_values(n: int, arr: Board, li: Tuple[Tuple, Tuple]):
    """Set += 1 on arr[li[0][0]][li[0][1]] and set other coords to 0"""
    i = 1;

    arr[li[0][0]][li[0][1]] += 1;
    while (i < len(li)):
        arr[li[i][0]][li[i][1]] = 0;
        i += 1;
#3.3[2]
def     fill_zero(n: int, arr: Board, coords: Tuple[int, int]) -> void:
    """Change zero by random value returned by generate_cell function"""
    i = 0;

    while ((coords[0] - i - 1) > -1):
        arr[coords[0] - i][coords[1]] = arr[coords[0] - 1 - i][coords[1]];
        i += 1;
    arr[coords[0] - i][coords[1]] = generate_cell((0.2,0.3,0.4));

def     remove_zeros(n: int, arr: Board, tupl: Tuple[int, int]):
    """Search for 0s to call fill_zero"""
    i = 0;
    j = 0;

    while (i < n):
        while (j < n):
            if (arr[i][j] == 0):
                fill_zero(n, arr, (i, j));
            j += 1
        i += 1
        j = 0

tupl = (2,2);
li = [tupl];
arr = [[8,8,69,8,1],[8,2,0,8,8],[4,8,0,8,3],[4,2,8,8,4],[4,2,8,1,6]];
print(arr)
get_adj_cells(5, arr, tupl, li);
print(arr)
change_cells_values(5, arr, li);
print(arr)
remove_zeros(5, arr, tupl);
print(arr)
