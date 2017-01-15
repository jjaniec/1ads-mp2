import pygame
from pygame.locals import *

WINDOW_SIZE = (500, 500)

def get_boardsize_GUI(rectpositions, rectssize):
    GREY = (165, 165, 165)
    font = pygame.font.SysFont('freesans', 36)
    rects = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    #rectangles / surfaces / texts renders / texts rectangles
    for i in range(len(rects[0])):
        rects[0][i] = pygame.Rect(rectpositions[i], rectssize)
        rects[1][i] = pygame.Surface(rects[0][i].size)
        rects[2][i] = font.render(str(i + 4) + " x " + str(i + 4), True, (0, 0, 0))
        rects[3][i] = rects[2][i].get_rect()
        rects[3][i].centerx = rects[1][i].get_rect().centerx
        rects[3][i].centery = rects[1][i].get_rect().centery
        rects[1][i].fill(GREY)
    while 1:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quit()
            if e.type == MOUSEBUTTONUP and e.button == 1:
                for i in range(len(rects[0])):
                    if rects[0][i].collidepoint(e.pos):
                        return (i + 4)
        window.fill((0, 0, 0))
        for i in range(len(rects[0])):
            window.blit(rects[1][i], rects[0][i])
            rects[1][i].blit(rects[2][i], rects[3][i])
        pygame.display.flip()

pygame.init()
window = pygame.display.set_mode(WINDOW_SIZE)
print(get_boardsize_GUI(((100, 100), (100, 200), (100, 300)), (200, 90)))
