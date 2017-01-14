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
    font = pygame.font.SysFont('freesans', 36)
    rect1_text = font.render("EASY", True, (0, 0, 0))
    rect2_text = font.render("MEDIUM", True, (0, 0, 0))
    rect3_text = font.render("HARD", True, (0, 0, 0))
    rect1_textrect = rect1_text.get_rect()
    rect1_textrect.centerx = rect1_surface.get_rect().centerx
    rect1_textrect.centery = rect1_surface.get_rect().centery
    rect2_textrect = rect2_text.get_rect()
    rect2_textrect.centerx = rect2_surface.get_rect().centerx
    rect2_textrect.centery = rect2_surface.get_rect().centery
    rect3_textrect = rect3_text.get_rect()
    rect3_textrect.centerx = rect3_surface.get_rect().centerx
    rect3_textrect.centery = rect3_surface.get_rect().centery
    rect1_surface.fill((0, 255, 0))
    rect2_surface.fill((255, 255, 0))
    rect3_surface.fill((255, 0, 0))

    while difficulty == (1, 1, 1):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quit()
            if e.type == MOUSEBUTTONUP and e.button == 1:
                if rect1.collidepoint(e.pos):
                    difficulty = EASY
                if rect2.collidepoint(e.pos):
                    difficulty = MEDIUM
                if rect3.collidepoint(e.pos):
                    difficulty = HARD

        window.fill((0, 0, 0)) #background
        window.blit(rect1_surface, rect1)
        rect1_surface.blit(rect1_text, rect1_textrect)
        window.blit(rect2_surface, rect2)
        rect2_surface.blit(rect2_text, rect2_textrect)
        window.blit(rect3_surface, rect3)
        rect3_surface.blit(rect3_text, rect3_textrect)
        pygame.display.flip()
    return (difficulty)

pygame.init()
window = pygame.display.set_mode(WINDOW_SIZE)
print(get_dificulty_GUI(((100, 100), (100, 200), (100, 300)), (200, 90)))
#pygame.quit()

