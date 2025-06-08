import pygame
import sys
import random

pygame.init()

TITLE_FONT = pygame.font.Font(None, 72)
SCORE_FONT = pygame.font.Font(None, 48)
INSTR_FONT = pygame.font.Font(None, 32)
GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)
WHITE = (255, 255, 255)
BUTTON_COLOR = (255, 215, 0)

CELL_SIZE = 44
NUM_CELLS = 14
OFFSET = 75
SCREEN_SIZE = 2 * OFFSET + CELL_SIZE * NUM_CELLS
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Duck Parade")
clock = pygame.time.Clock()

# images
duck_img = pygame.image.load("duck.png").convert_alpha()
duck_img = pygame.transform.scale(duck_img, (CELL_SIZE, CELL_SIZE))
# Entity Class
#subclass
#Game class
#Game loop
#Drawing
