from typing import Tuple, Callable, TypeVar, Any, List, Optional, Dict
from math import floor
import pygame
from pygame.locals import *

# Type aliases
Surface = TypeVar('Surface')
Event = TypeVar('Event')
Clock = TypeVar('Clock')
Coord = Tuple[int, int]
Row = List[int]
Board = List[Row]
Color = Tuple[int, int, int]

def setup(window_dim: Tuple[int, int],
          window_caption: str,
          additional_setup: Optional[Callable] = None) -> Tuple[Surface, Clock]:
    """Initialize Pygame and a window with the given dimensions. Also set up the
    clock object. Additional setup can be done with an optional provided
    function.
    """

    pygame.init()
    window = pygame.display.set_mode(window_dim)
    pygame.display.set_caption(window_caption)
    clock = pygame.time.Clock()
    if additional_setup is not None:
        additional_return = additional_setup(window, clock)

    return window, clock

def drawer(window: Surface,
           clock: Clock,
           fps: int,
           draw: Callable[[Surface, List], None],
           manage_events: Callable[[List[Event]], List]) -> None:
    """Abstract the main loop by just having to specify the main window, the
    clock object, frames per second, the draw routine that will manage every
    sketching on the window and a function that will manage the events and
    compute the changes that will be drawn in then next frame.
    """

    mutations = []
    while True:
        draw(window, mutations)
        mutations = manage_events(pygame.event.get())
        if mutations[0]:
            pygame.display.flip() # Actualize display
            clock.tick(fps)
        else:
            break

def cell_drawer(board: Board,
                surface: Surface) -> Callable[[Coord], None]:
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
        cell_color = cell_colors[value]
        font_color = map(lambda v: 255 - v, cell_color)
        font_surface = font.render(str(value), True, font_color)
        font_rect = font_surface.get_rect(center=((x + 0.5) * cell_width,
                                                  (y + 0.5) * cell_height))

        pygame.draw.rect(surface, cell_color, cell_rect)
        surface.blit(font_surface, font_rect) # Paste the font surface onto the
                                              # cell

    return draw_cell

def draw_these_cells(draw_cell: Callable[[Coord], None],
                     cells: List[Coord]) -> None:
    """Draw a list of cells by employing the provided cell drawing procedure."""

    for cell in cells:
        draw_cell(cell)

def draw_board(draw_cell: Callable[[Coord], None], board_length: int) -> None:
    """Provided a cell drawing procedure and the length of the board, calls the
    earlier on each coordinate of the board.
    """

    r = range(board_length)
    for y in r:
        for x in r:
            draw_cell((x, y))

def draw(window: Surface, changes: List) -> None:
    """This procedure takes the care of drawing everything we want inside our
    window. The changes dictionary contains a list of additonal distortions that
    it have apply to the drawings.
    """

    board = [
        [1, 4, 2, 3],
        [5, 1, 1, 1],
        [1, 1, 1, 9],
        [2, 2, 2, 1]
    ]
    draw_board(cell_drawer(board, window), len(board))

def manage_events(events: List[Event]) -> List: # TODO
    """Given a list of event, compute a list of changes to be applied at the
    next draw call (i.e. the next frame), while modifying the board if the event
    list ends up bringing the need to."""

    raise Warning("TODO: manage_events is not yet implemented.")
    return [False]

if __name__ == "__main__":
    window, clock = setup((1000, 1000), "Just Get 10")
    drawer(window, clock, 60, draw, manage_events)
