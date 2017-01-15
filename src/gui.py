"""This file contains all routines to render the GUI and process user inputs."""

from typing import Tuple, Callable, TypeVar, Any, List, Optional, Dict
from math import floor
from functools import partial

import pygame
from pygame.locals import *

from basis import generate_board
from possible import is_board_still_playable, maximum_value_in_board
from merge import get_similar_cells_suite, merge_cells, fall_and_fill

# Type aliases
Surface = TypeVar('Surface')
Event = TypeVar('Event')
Clock = TypeVar('Clock')
Coord = Tuple[int, int]
Color = Tuple[int, int, int, Optional[int]]
Row = List[int]
Board = List[Row]
WindowSurfaces = Dict[Surface, Surface]

# Extended Events
RENDER_WINDOW = 0
RENDER_SELECTION = 1
RENDER_WIN = 2
RENDER_LOOSE = 3
RESET_GAME = 4
DEFER_EVENT = 5
WIN_LOOSE_DONE = 6

def setup(window_dim: Tuple[int, int],
          window_caption: str) -> Tuple[WindowSurfaces, Clock]:
    """Initialize Pygame and a window with the given dimensions. Also set up the
    clock object.
    """

    pygame.init()
    window = pygame.display.set_mode(window_dim)
    pygame.display.set_caption(window_caption)
    board_rect = pygame.Rect((0, 0), (window_dim[0] / 3 * 2, window_dim[1]))
    board = window.subsurface(board_rect)
    menu_rect = pygame.Rect((1000, 0), (window_dim[0] / 3, window_dim[1]))
    menu = window.subsurface(menu_rect)
    surfaces = { "window": window, "board": board, "menu": menu }
    clock = pygame.time.Clock()

    return surfaces, clock

def drawer(surfaces: WindowSurfaces,
           clock: Clock,
           fps: int,
           board: Board,
           process_render_events: Callable[[WindowSurfaces, Board, List[Event]], None],
           process_user_events: Callable[[WindowSurfaces, Board, List[Event]], bool]
           ) -> None:
    """Abstract the main loop by just having to specify the main window, the
    clock object, frames per second, the game board and the event rendering
    routine that will manage every sketching on the window according to the ones
    inside the event queue.
    """

    post_event(USEREVENT, RENDER_WINDOW) # Initial rendering of the entire window
    while True:
        events = pygame.event.get()
        process_defered_events(events)
        process_render_events(surfaces, board, events)
        pass_next_frame = process_user_events(surfaces, board, events)
        if pass_next_frame:
            clock.tick(fps)
        else:
            break

def post_event(event_type: int, extended_type: int = -1,
               attributes: Optional[Dict] = {}) -> None:
    """Little utility to queue up an event with less prose."""

    attributes["extended_type"] = extended_type
    pygame.event.post(pygame.event.Event(event_type, attributes))

def defer_event(event_type: int, extended_type: int, frames: int) -> None:
    """Emit a defered event that will emit another envent with event_type in the
    number of frames provided.
    """

    post_event(USEREVENT, DEFER_EVENT,
               { "defered_type": event_type,
                 "defered_extended_type": extended_type,
                 "frames": frames })

def process_defered_events(events: List[Event]) -> None:
    """Take care of decrementing the number of frames in which defered event
    will get emitted. Emit these defered events when their frames number is 0.
    """

    for event in events:
        if event.type is USEREVENT and event.extended_type is DEFER_EVENT and event.frames > 0:
            post_event(USEREVENT, DEFER_EVENT,
                       { "defered_type": event.defered_type,
                         "defered_extended_type": event.defered_extended_type,
                         "frames": event.frames - 1 })
        elif event.type is USEREVENT and event.extended_type is DEFER_EVENT and event.frames is 0:
            post_event(event.defered_type, event.defered_extended_type)

def process_render_events(surfaces: WindowSurfaces,
                          board: Board,
                          events: List[Event]) -> None:
    """This procedure takes the care of drawing everything we want inside our
    window according the RENDER_* events received.
    """

    draw_cell = cell_drawer(surfaces["board"], board)
    draw_selected_cell = partial(draw_cell, selected=True)
    write_text = partial(draw_centered_text, surface=surfaces["board"],
                         font_name='Fixedsys', color=(255, 255, 255))
    for event in events:
        if event.type is USEREVENT and event.extended_type is RENDER_WINDOW:
            clear(surfaces["window"])
            draw_board(draw_cell, len(board))
            draw_menu(surfaces["menu"], board)
        elif event.type is USEREVENT and event.extended_type is RENDER_SELECTION:
            draw_these_cells(draw_selected_cell, event.selected_cells)
        elif event.type is USEREVENT and event.extended_type is RENDER_WIN:
            clear(surfaces["window"]) # Erase everything
            write_text(text="YOU WIN")
            draw_menu(surfaces["menu"], board)
            post_event(USEREVENT, WIN_LOOSE_DONE)
        elif event.type is USEREVENT and event.extended_type is RENDER_LOOSE:
            clear(surfaces["window"]) # Erase everything
            write_text(text="YOU LOOSE")
            draw_menu(surfaces["menu"], board)
            post_event(USEREVENT, WIN_LOOSE_DONE)

    pygame.display.flip() # Actualize display

def process_user_events(surfaces: WindowSurfaces,
                        board: Board,
                        events: List[Event]) -> bool:
    """Every user-related events are processed here, setting off other events
    depending on the case, as a RENDER_BOARD event for instance.
    """

    win_loose_done = False
    for event in events:
        if event.type is QUIT:
            return False # Abort
        elif event.type is MOUSEBUTTONUP:
            if event.pos[0] <= surfaces["board"].get_width():
                cell = get_coord_in_grid_from_pos(surfaces["board"], event.pos,
                                                  len(board), len(board))
                selected_cells = [ cell ]
                get_similar_cells_suite(board, cell, selected_cells)
                post_event(USEREVENT, RENDER_WINDOW) # Whatever happens, we will
                                                    # need to redraw the entire
                                                    # window
                # Already selected
                if surfaces["board"].get_at(event.pos) == (255, 255, 255, 255):
                    merge_cells(board, selected_cells)
                    fall_and_fill(board, (0.125, 0.25, 0.5))
                # Not yet selected, and is a suite of similar cells
                elif len(selected_cells) > 1:
                    post_event(USEREVENT, RENDER_SELECTION,
                               { "selected_cells": selected_cells })
            else:
                clicked_button = get_coord_in_grid_from_pos(surfaces["menu"],
                                                            event.pos, 1, 3)[1]
                if clicked_button == 0: # Score button
                    pass # Nothing
                elif clicked_button == 1: # Reset button
                    post_event(USEREVENT, RESET_GAME)
                elif clicked_button == 2: # Quit button
                    post_event(QUIT)
        elif event.type is USEREVENT and event.extended_type is RESET_GAME:
            n = len(board)
            new_board = generate_board(n, (0.125, 0.25, 0.5))
            for i in range(n):
                board[i] = new_board[i]
            post_event(USEREVENT, RENDER_WINDOW)
        elif event.type is USEREVENT and event.extended_type is WIN_LOOSE_DONE:
            win_loose_done = True
            if (maximum_value_in_board(board) is 10 or
                    not is_board_still_playable(board)):
                post_event(USEREVENT, WIN_LOOSE_DONE)


    # Win/loose condition
    if not win_loose_done:
        if maximum_value_in_board(board) is 10:
            post_event(USEREVENT, RENDER_WIN)
        elif not is_board_still_playable(board):
            post_event(USEREVENT, RENDER_LOOSE)

    return True

def get_coord_in_grid_from_pos(surface, pos, w_sep, h_sep):

    cell_width = surface.get_width() / w_sep
    cell_height = surface.get_height() / h_sep
    x = floor(pos[0] / cell_width)
    y = floor(pos[1] / cell_height)
    return (x, y)

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
    def draw_cell(cell: Coord, selected: Optional[bool] = False) -> None:
        x = cell[0]
        y = cell[1]
        value = board[y][x]

        cell_position = (cell_width * x, cell_height * y)
        cell_rect = (cell_position, cell_dimensions)
        cell_color = cell_colors[0 if selected else value]
        cell_surface = container.subsurface(cell_rect)
        cell_surface.fill(cell_color)

        font_color = (0, 0, 0) if selected else (255, 255, 255)

        draw_centered_text(cell_surface, 'Fixedsys', font_color, str(value))

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

def draw_centered_text(surface: Surface, font_name: str, color: Color,
                       text: str) -> None:
    """Draw text with font and color at the center of surface. The font size is
    automatically determined.
    """

    font_size = floor(surface.get_width() / 4)
    font = pygame.font.Font(pygame.font.match_font(font_name), font_size)
    font_surface = font.render(text, True, color)
    font_position = font_surface.get_rect(center=(0.5 * surface.get_width(),
                                                  0.5 * surface.get_height()))
    surface.blit(font_surface, font_position)

def draw_menu(surface: Surface, board: Board) -> None:
    """Draw the game menu onto surface."""

    score = maximum_value_in_board(board)
    full_width = surface.get_width()
    full_height = surface.get_height()
    button_rect = pygame.Rect((0, 0), (full_width, full_height / 3))
    score_button = generate_button("Score: " + str(score), surface, button_rect)
    reset_button_rect = button_rect.move(0, 333)
    reset_button = generate_button("Reset", surface, reset_button_rect)
    quit_button_rect = button_rect.move(0, 666)
    quit_button = generate_button("Quit", surface, quit_button_rect)

def generate_button(text: str, container: Surface, rect) -> Surface:

    button_surface = container.subsurface(rect)
    button_surface.fill((255, 255, 255))
    draw_centered_text(button_surface, 'Fixedsys', (0, 0, 0), text)
    return button_surface

def clear(surface):
    """Fill surface with black."""

    surface.fill((0, 0, 0))

if __name__ == "__main__":
    board = generate_board(5, (0.125, 0.25, 0.5))
    surfaces, clock = setup((1500, 1000), "Just Get 10")
    drawer(surfaces, clock, 60, board, process_render_events,
           process_user_events)
