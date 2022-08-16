import pygame
from settings import *
from level import Level
from gamedata import level_0

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Conqueror')
icon = pygame.image.load('../graphics/terrain/sword.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
bg = pygame.image.load('../graphics/terrain/sword background.jpg')
active = True
keys = pygame.key.get_pressed()

level = Level(level_0, screen)

# while True:
#     # event loop
#     screen.blit(bg, (0, 0))
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

# level.run()

#     # drawing logic
#     pygame.display.update()
#     clock.tick(60)

while active:

    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    level.run()

    pygame.display.update()
    clock.tick(60)
