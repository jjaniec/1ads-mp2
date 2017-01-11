import os.path
import io
from typing import Tuple, List

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
#    if (os.path.exists(path)):
        #print("Found an existing save file\nWould you start a new game or continue the existing one ?")
    return (os.path.exists(path))

def     get_saved_board(path: str) -> str:
    file_ = open(path)
    print(file_.read())
    return (file_.read())

save_board("xDDDD", fullpath)
print(str(lf_existing_saves(fullpath)))
get_saved_board(fullpath)
