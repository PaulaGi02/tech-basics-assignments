# importing required library
import pygame
import random

# constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BACKGROUND_COLOR = (255,255,255)

# activate the pygame library
pygame.init()

# create the display surface object
# of specific dimension.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# set the pygame window name
pygame.display.set_caption('The Scream Bouncing')

# create a surface object, image is drawn on it.
# use convert_alpha() for png images
scream = pygame.image.load("scream.jpg").convert_alpha()
scream = pygame.transform.scale(scream, (167,300))
scream_rect = scream.get_rect()

#set position
scream_rect.x = SCREEN_WIDTH // 2
scream_rect.y = SCREEN_HEIGHT // 2

# option: tint your image if you want
# imp.fill((0, 0, 200, 100), special_flags=pygame.BLEND_ADD)

# position of dino
scream_x = 100
scream_y = 100

# Init the clock
clock = pygame.time.Clock()

flag = True
while flag:
    # ticking the clock
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    # moving dino as clock tick
    if scream_x  < SCREEN_WIDTH:
        scream_x += 3
    else:
        scream_x = 0

    # paint the screen with background color
    screen.fill(BACKGROUND_COLOR)
    # Using blit to copy image to screen at a specific location
    screen.blit(scream, (scream_x, scream_y))
    # refresh the display
    pygame.display.flip()

pygame.quit()
exit(0)