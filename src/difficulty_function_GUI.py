import pygame
from pygame.locals import *

WINDOW_SIZE = (500, 500)

def     get_dificulty_GUI(rectspositions, rectssize):
    GREY = (165, 165, 165)

    rect1 = pygame.Rect(rectspositions[0], rectssize)
    rect2 = pygame.Rect(rectspositions[1], rectssize)
    rect3 = pygame.Rect(rectspositions[2], rectssize)
    rect1_surface = pygame.Surface(rect1.size)
    rect2_surface = pygame.Surface(rect2.size)
    rect3_surface = pygame.Surface(rect3.size)
    font = pygame.font.SysFont('freesans', 36)
    rect1_text = font.render("4 x 4", True, (0, 0, 0))
    rect2_text = font.render("5 x 5", True, (0, 0, 0))
    rect3_text = font.render("6 x 6", True, (0, 0, 0))
    rect1_textrect = rect1_text.get_rect()
    rect1_textrect.centerx = rect1_surface.get_rect().centerx
    rect1_textrect.centery = rect1_surface.get_rect().centery
    rect2_textrect = rect2_text.get_rect()
    rect2_textrect.centerx = rect2_surface.get_rect().centerx
    rect2_textrect.centery = rect2_surface.get_rect().centery
    rect3_textrect = rect3_text.get_rect()
    rect3_textrect.centerx = rect3_surface.get_rect().centerx
    rect3_textrect.centery = rect3_surface.get_rect().centery
    rect1_surface.fill(GREY)
    rect2_surface.fill(GREY)
    rect3_surface.fill(GREY)

    while 1:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quit()
            if e.type == MOUSEBUTTONUP and e.button == 1:
                if rect1.collidepoint(e.pos):
                    return (4)
                if rect2.collidepoint(e.pos):
                    return (5)
                if rect3.collidepoint(e.pos):
                    return (6)

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

