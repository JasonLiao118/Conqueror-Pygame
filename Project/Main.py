# Simple pygame program

# Import and initialize the pygame library
import pygame
from settings import *
from level import Level

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1200, 700])
level = Level(level_map, screen)

#Title and Icon
pygame.display.set_caption("Basic Game")
icon = pygame.image.load('character.png')
pygame.display.set_icon(icon)

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((0, 0, 0))

    # run
    level.run()

    pygame.display.update()

# Done! Time to quit.
pygame.quit()
