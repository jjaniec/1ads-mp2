from typing import Tuple, Callable, TypeVar, Any, List, Optional
from math import floor
import pygame
from pygame.locals import *

Surface = TypeVar('Surface')
Event = TypeVar('Event')
Clock = TypeVar('Clock')
Coord = Tuple[int, int]
Row = List[int]
Board = List[Row]
Color = Tuple[int, int, int]

def setup(window_dim: Tuple[int, int], window_caption: str,
          additional_setup: Optional[Callable] = None) -> Tuple[Surface, Clock]:
    pygame.init()
    window = pygame.display.set_mode(window_dim)
    pygame.display.set_caption(window_caption)
    clock = pygame.time.Clock()
    if additional_setup is not None:
        additional_return = additional_setup(window, clock)

    return window, clock

def drawer(window: Surface, clock: Clock, fps: int,
           draw: Callable[[Surface, List[Event]], bool]) -> None:
    while True:
        pass_to_next_frame = draw(window, pygame.event.get())
        if pass_to_next_frame:
            pygame.display.flip()
            clock.tick(fps)
        else:
            break

def cell_drawer(board: Board,
                surface: Surface) -> Callable[[Coord], None]:
    cell_colors = (
        (255, 255, 255), # selected
        (100, 202, 129), # 1
        (34, 97, 176), # 2
        (10, 130, 159), # 3
        (217, 162, 91), # 4
        (217, 162, 164), # 5
        (76, 10, 53), # 6
        (141, 22, 16), # 7
        (127, 70, 104), # 8
        (218, 205, 225), # 9
        (218, 205, 225), # 10
    )
    board_area = len(board)
    cell_width = surface.get_width() / board_area
    cell_height = surface.get_height() / board_area
    font_size = floor(cell_width / 4)
    font = pygame.font.Font(pygame.font.match_font('Fixedsys'), font_size)
    def draw_cell(cell: Coord):
        x = cell[0]
        y = cell[1]
        value = board[y][x]
        cell_rect = (x * cell_width, y * cell_height, cell_width, cell_height)
        pygame.draw.rect(surface, cell_colors[value], cell_rect)
        font_surface = font.render(str(value), True, (255, 255, 255))
        font_rect = font_surface.get_rect(center=((x + 0.5) * cell_width,
                                                  (y + 0.5) * cell_height))
        surface.blit(font_surface, font_rect)

    return draw_cell

def draw_these_cells(draw_cell: Callable, cells: List[Coord]) -> None:
    for cell in cells:
        draw_cell(cell)

def draw_board(board, draw_cell) -> None:
    n = len(board)
    for y in range(n):
        for x in range(n): draw_cell((x, y))

def draw(surface, events):
    for event in events:
        if event.type is QUIT:
            return False
    board = [
        [1, 4, 2, 3],
        [5, 1, 1, 1],
        [1, 1, 1, 9],
        [2, 2, 2, 1]
    ]
    draw_board(board, cell_drawer(board, surface))
    return True

if __name__ == "__main__":
    window, clock = setup((300, 300), "Just Get 10")
    drawer(window, clock, 60, draw)
