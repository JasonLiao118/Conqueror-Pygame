import pygame
from settings import tile_size
from support import import_csv_layout, import_cut_graphics
from tiles import Tile, StaticTile

# from player import Player


class Level:
    def __init__(self, level_data, surface):

        # general setup
        self.display_surface = surface
        self.world_shift = 0

        # terrain setup
        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(
            terrain_layout, 'terrain')

        # background setup
        background_layout = import_csv_layout(level_data['background'])
        self.background_sprites = self.create_tile_group(
            background_layout, 'background')

        # decorations setup
        decorations_layout = import_csv_layout(level_data['decorations'])
        self.decorations_sprites = self.create_tile_group(
            decorations_layout, 'decorations')

    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if type == 'terrain':
                        terrain_tile_list = import_cut_graphics(
                            '../graphics/terrain/ProjectUtumno_full.png')
                        tile_surface = terrain_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)

                    if type == 'background':
                        background_tile_list = import_cut_graphics(
                            '../graphics/terrain/ProjectUtumno_full.png')
                        tile_surface = background_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)

                    if type == 'decorations':
                        decorations_tile_list = import_cut_graphics(
                            '../graphics/terrain/ProjectUtumno_full.png')
                        tile_surface = decorations_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)

                    sprite_group.add(sprite)

        return sprite_group

    def run(self):

        # run the entire game/level

        # terrain
        self.terrain_sprites.update(self.world_shift)
        self.terrain_sprites.draw(self.display_surface)

        # background
        self.background_sprites.update(self.world_shift)
        self.background_sprites.draw(self.display_surface)

        # decorations
        self.decorations_sprites.update(self.world_shift)
        self.decorations_sprites.draw(self.display_surface)


# class Level:
#     def __init__(self):

#         # level setup
#         self.display_surface = pygame.display.get_surface()

#         # sprite group setup
#         self.visible_sprites = CameraGroup()
#         self.active_sprites = pygame.sprite.Group()
#         self.collision_sprites = pygame.sprite.Group()

#         self.setup_level()

#     def setup_level(self):
#         for row_index, row in enumerate(LEVEL_MAP):
#             for col_index, col in enumerate(row):
#                 x = col_index * TILE_SIZE
#                 y = row_index * TILE_SIZE
#                 if col == 'X':
#                     Tile((x, y), [self.visible_sprites,
#                          self.collision_sprites])
#                 if col == 'P':
#                     self.player = Player(
#                         (x, y), [self.visible_sprites, self.active_sprites], self.collision_sprites)

#     def run(self):
#         # run the entire game (level)
#         self.active_sprites.update()
#         self.visible_sprites.custom_draw(self.player)


# class CameraGroup(pygame.sprite.Group):
#     def __init__(self):
#         super().__init__()
#         self.display_surface = pygame.display.get_surface()
#         self.offset = pygame.math.Vector2(100, 300)

#         # camera
#         cam_left = CAMERA_BORDERS['left']
#         cam_top = CAMERA_BORDERS['top']
#         cam_width = self.display_surface.get_size(
#         )[0] - (cam_left + CAMERA_BORDERS['right'])
#         cam_height = self.display_surface.get_size(
#         )[1] - (cam_top + CAMERA_BORDERS['bottom'])

#         self.camera_rect = pygame.Rect(
#             cam_left, cam_top, cam_width, cam_height)

#     def custom_draw(self, player):

#         # getting the camera position
#         if player.rect.left < self.camera_rect.left:
#             self.camera_rect.left = player.rect.left
#         if player.rect.right > self.camera_rect.right:
#             self.camera_rect.right = player.rect.right
#         if player.rect.top < self.camera_rect.top:
#             self.camera_rect.top = player.rect.top
#         if player.rect.bottom > self.camera_rect.bottom:
#             self.camera_rect.bottom = player.rect.bottom

#         # camera offset
#         self.offset = pygame.math.Vector2(
#             self.camera_rect.left - CAMERA_BORDERS['left'],
#             self.camera_rect.top - CAMERA_BORDERS['top'])

#         for sprite in self.sprites():
#             offset_pos = sprite.rect.topleft - self.offset
#             self.display_surface.blit(sprite.image, offset_pos)
