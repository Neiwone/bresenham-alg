import pygame
import time
from constants import *

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_NAME)
clock = pygame.time.Clock()

pygame.font.init()
FONT = pygame.font.SysFont('Arial', 8)

def draw_grid():
    screen.fill('black')
    for h in range(GRID_SIZE):
        for w in range(GRID_SIZE):
            if GRID[w][h] == 'p':
                pygame.draw.rect(screen, 'red', pygame.Rect(25*h, 25*w, 25, 25))
            if GRID[w][h] == 'w':
                pygame.draw.rect(screen, 'grey', pygame.Rect(25*h, 25*w, 25, 25))
            text = FONT.render(f'{GRID_SIZE - w - 1}, {h}', False, 'yellow')      
            pygame.draw.rect(screen, 'white', pygame.Rect(25*h, 25*w, 25, 25), 2)
            screen.blit(text, ((h*25, w*25)))
            


def draw_line(x1, y1, x2, y2):
    DX = x2 - x1
    DY = y2 - y1

    d = 2*DY - DX

    DELTA_E, DELTA_NE = 2*DY, 2*(DY - DX)
    x, y = x1, y1

    while x != x2 and y != y2:
        print(f'x: {x}, y: {y}, d: {d}')
        if x != x1 and y != y2:
            GRID[GRID_SIZE - y - 1][x] = 'w'
        if d <= 0:
            d += DELTA_E
            x += 1
        else: 
            d += DELTA_NE
            x += 1
            y += 1

        


running = True
has_draw_line = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False



    draw_grid()
    if not has_draw_line:
        draw_line(1, 1, 14, 10)
        has_draw_line = True
        
    pygame.display.flip()

    clock.tick(60)
    

pygame.quit()
