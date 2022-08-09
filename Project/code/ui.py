import pygame


class UI:
    def __init__(self, surface):

        # setup
        self.display_surface = surface

        # health
        self.health_bar = pygame.image.load('../graphics/character/hp.png')

        # points
        self.points = pygame.image.load('../graphics/character/hp.png')

    def show_health(self, current, full):
        self.display_surface.blit(self.health_bar, (500, 975))

    def show_points(self, amount):
        pass
