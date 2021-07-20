import pygame

pygame.init()
pygame.font.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

FPS = 60

WIDTH, HEIGHT = 600, 700

ROWS = COLS = 50

TOOLBAT_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH // COLS

BG_COLOR = WHITE

DRAW_GRID_LINES = False

def get_font(size):
    return pygame.font.SysFont("comicsans", size)