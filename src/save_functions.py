import os.path
from typing import List

Row = List[int]
Board = List[Row]

filename = "save.savefile"
path = "./"
fullpath = path + filename

def     save_board(arr: Board, path: str) -> None:
    """save current board in a file"""
    file_ = open(path, "w")
    file_.write(str(arr))
    file_.close()

def     lf_existing_saves(path: str) -> bool:
    """check if a savefile already exists"""
    return os.path.exists(path)

def     get_saved_board(path: str) -> str:
    """return saved board"""
    file_ = open(path)
    return file_.read()

#arr2 = []
#exec("arr2 = " + get_saved_board(fullpath))
#print(arr2)
