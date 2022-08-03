
# import pygame
# from settings import *


# class Tile(pygame.sprite.Sprite):
#     def __init__(self, pos, groups):
#         super().__init__(groups)
#         self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
#         self.image.fill(TILE_COLOR)
#         self.rect = self.image.get_rect(topleft=pos)

import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, shift):
        self.rect.x += shift


class StaticTile(Tile):
    def __init__(self, size, x, y, surface):
        super().__init__(size, x, y)
        self.image = surface


# class AnimatedTile(Tile):
#     def __init__(self, size, x, y, path):
#         super().__init__(size, x, y)
#         self.frames = import_folder(path)
