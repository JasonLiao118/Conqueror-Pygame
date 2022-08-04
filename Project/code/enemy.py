import pygame

from tiles import StaticTile
# from tiles import AnimatedTile
from random import randint


class Enemy(StaticTile):
    # def __init__(self, size, x, y):
    #     super().__init__(size, x, y, '../graphics/terrain/ProjectUtumno_full.png')
    def __init__(self, size, x, y, surface):
        super().__init__(size, x, y)
        self.image = surface
        self.rect.y += size - self.image.get_size()[1]
        self.speed = randint(3, 5)

    def move(self):
        self.rect.x += self.speed

    def update(self, shift):
        self.rect.x += shift
        self.move()
