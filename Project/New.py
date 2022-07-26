# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([800, 600])

#Title and Icon
pygame.display.set_caption("Basic Game")
icon = pygame.image.load('character.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('swordsman.png')
playerX = 170
playerY = 100
player_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))

    # Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    player(playerX, playerY)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
