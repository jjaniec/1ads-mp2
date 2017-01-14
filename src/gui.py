"""This file contains all routines to render the GUI and process user inputs."""

from typing import Tuple, Callable, TypeVar, Any, List, Optional, Dict
from math import floor

import pygame
from pygame.locals import *

from basis import generate_board

# Type aliases
Surface = TypeVar('Surface')
Event = TypeVar('Event')
Clock = TypeVar('Clock')
Coord = Tuple[int, int]
Row = List[int]
Board = List[Row]

# Events
RENDER_BOARD = USEREVENT + 1

def setup(window_dim: Tuple[int, int],
          window_caption: str) -> Tuple[Surface, Clock]:
    """Initialize Pygame and a window with the given dimensions. Also set up the
    clock object.
    """

    pygame.init()
    window = pygame.display.set_mode(window_dim)
    pygame.display.set_caption(window_caption)
    clock = pygame.time.Clock()

    return window, clock

def drawer(window: Surface,
           clock: Clock,
           fps: int,
           board: Board,
           render_events: Callable[[Surface, Board, List[Event]], bool]) -> None:
    """Abstract the main loop by just having to specify the main window, the
    clock object, frames per second, the game board and the event rendering
    routine that will manage every sketching on the window according to the ones
    inside the event queue.
    """

    post_event(RENDER_BOARD) # Initial rendering of the board
    while True:
        events = pygame.event.get()
        process_render_events(window, board, events)
        pass_next_frame = process_user_events(window, board, events)
        if pass_next_frame:
            clock.tick(fps)
        else:
            break

def post_event(event_type: int, attributes: Optional[Dict] = {}) -> None:
    """Little utility to queue up an event with less prose."""

    pygame.event.post(pygame.event.Event(event_type, attributes))

def process_render_events(window: Surface,
                          board: Board,
                          events: List[Event]) -> None:
    """This procedure takes the care of drawing everything we want inside our
    window according the RENDER_* events received.
    """

    draw_cell = cell_drawer(window, board)
    for event in events:
        if event.type is RENDER_BOARD:
            window.fill((0, 0, 0))
            draw_board(draw_cell, len(board))

    pygame.display.flip() # Actualize display

def process_user_events(window: Surface,
                        board: Board,
                        events: List[Event]) -> bool:
    """Every user-related events are processed here, setting off other events
    depending on the case, as a RENDER_BOARD event for instance.
    """

    for event in events:
        if event.type is QUIT:
            return False # Abort

    return True

def cell_drawer(container: Surface,
                board: Board) -> Callable[[Coord, Optional[bool]], None]:
    """Higher order function that enables the construction of cell drawing
    procedure that only needs the coordinates of a cell inside the game board as
    a paramater.
    """

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
        (218, 205, 225) # 10
    )

    n = len(board)
    cell_width = container.get_width() / n
    cell_height = container.get_height() / n
    cell_dimensions = (cell_width, cell_height)
    font_size = floor(cell_width / 4)
    font = pygame.font.Font(pygame.font.match_font('Fixedsys'), font_size)
    def draw_cell(cell: Coord, selected: Optional[bool] = False) -> None:
        x = cell[0]
        y = cell[1]
        value = board[y][x]

        cell_position = (cell_width * x, cell_height * y)
        cell_rect = (cell_position, cell_dimensions)
        cell_color = cell_colors[0 if selected else value]
        cell_surface = pygame.Surface(cell_dimensions)
        cell_surface.fill(cell_color)

        font_color = (0, 0, 0) if selected else (255, 255, 255)
        font_surface = font.render(str(value), True, font_color)
        font_position = font_surface.get_rect(center=((0.5) * cell_width,
                                                      (0.5) * cell_height))

        cell_surface.blit(font_surface, font_position) # Paste the font surface
                                                       # onto the cell's one
        container.blit(cell_surface, cell_rect)

    return draw_cell

def draw_these_cells(draw_cell: Callable[[Coord, Optional[bool]], None],
                     cells: List[Coord]) -> None:
    """Draw a list of cells by employing the provided cell drawing procedure."""

    for cell in cells:
        draw_cell(cell)

def draw_board(draw_cell: Callable[[Coord, Optional[bool]], None],
               board_length: int) -> None:
    """Provided a cell drawing procedure and the length of the board, calls the
    former on each coordinate of the board.
    """

    r = range(board_length)
    for y in r:
        for x in r:
            draw_cell((x, y))

if __name__ == "__main__":
    board = generate_board(5, (0.125, 0.25, 0.5))
    window, clock = setup((1000, 1000), "Just Get 10")
    drawer(window, clock, 60, board, render_events)
