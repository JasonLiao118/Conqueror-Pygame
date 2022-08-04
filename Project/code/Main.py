import pygame
import sys
from settings import *
from level import Level
from gamedata import level_0

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Dungeon')
clock = pygame.time.Clock()

level = Level(level_0, screen)

while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    level.run()

    # drawing logic
    pygame.display.update()
    clock.tick(60)
