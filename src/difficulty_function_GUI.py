import pygame
from pygame.locals import *

WINDOW_SIZE = (500, 500)

def     get_dificulty_GUI(rectspositions, rectssize):
    print(rectspositions[0])
    difficulty = (1, 1, 1)
    EASY = (0.1, 0.2, 0.3)
    MEDIUM = (0.2, 0.3, 0.4)
    HARD = (0.3, 0.4, 0.5)

    rect1 = pygame.Rect(rectspositions[0], rectssize)
    rect2 = pygame.Rect(rectspositions[1], rectssize)
    rect3 = pygame.Rect(rectspositions[2], rectssize)
    rect1_surface = pygame.Surface(rect1.size)
    rect2_surface = pygame.Surface(rect2.size)
    rect3_surface = pygame.Surface(rect3.size)
    rect1_surface.fill((0, 255, 0))
    rect2_surface.fill((255, 255, 0))
    rect3_surface.fill((255, 0, 0))

    while difficulty == (1, 1, 1):
        window.fill(0)
        window.blit(rect1_surface, rect1)
        window.blit(rect2_surface, rect2)
        window.blit(rect3_surface, rect3)
        pygame.display.flip()

    return (difficulty)

pygame.init()
window = pygame.display.set_mode(WINDOW_SIZE)
print(get_dificulty_GUI(((100, 100), (100, 200), (100, 300)), (200, 90)))
#pygame.quit()

