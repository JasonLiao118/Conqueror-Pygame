import pygame
from settings import tile_size, screen_height
from support import import_csv_layout, import_cut_graphics
from tiles import Tile, StaticTile
from enemy import Enemy
from player import Player
from particles import ParticleEffect
from ui import UI


class Level:
    def __init__(self, level_data, surface):

        # player stats
        self.max_health = 100
        self.cur_health = 100
        self.points = 0

        # user interface
        # self.ui = UI(surface)
        # self.ui.show_health(50, 100)

        # general setup
        self.display_surface = surface
        self.world_shift = 0
        self.current_x = 0

        # player
        player_layout = import_csv_layout(level_data['player'])
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.player_setup(player_layout)

        # dust
        self.dust_sprite = pygame.sprite.GroupSingle()
        self.player_on_ground = False

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

        # enemy
        enemy_layout = import_csv_layout(level_data['enemies'])
        self.enemy_sprites = self.create_tile_group(enemy_layout, 'enemies')

        # constraint
        constraint_layout = import_csv_layout(level_data['constraints'])
        self.constraint_sprites = self.create_tile_group(
            constraint_layout, 'constraint')

    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = (row_index - 192) * tile_size

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

                    if type == 'enemies':
                        sprite = Enemy(tile_size, x, y)

                    if type == 'constraint':
                        sprite = Tile(tile_size, x, y)

                    sprite_group.add(sprite)

        return sprite_group

    def player_setup(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                x = col_index * tile_size
                y = (row_index - 192) * tile_size
                if val == '0':
                    sprite = Player((x, y), self.display_surface,
                                    self.create_jump_particles)
                    self.player.add(sprite)
                if val == '1':
                    sword = pygame.image.load(
                        '../graphics/terrain/sword.png').convert_alpha()
                    sprite = StaticTile(tile_size, x, y, sword)
                    self.goal.add(sprite)

    def enemy_collision_reverse(self):
        for enemy in self.enemy_sprites.sprites():
            if pygame.sprite.spritecollide(enemy, self.constraint_sprites, False):
                enemy.reverse()

    def create_jump_particles(self, pos):
        if self.player.sprite.facing_right:
            pos -= pygame.math.Vector2(10, 5)
        else:
            pos += pygame.math.Vector2(10, -5)
        jump_particle_sprite = ParticleEffect(pos, 'jump')
        self.dust_sprite.add(jump_particle_sprite)

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.terrain_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right

        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.terrain_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0.1:
            player.on_ceiling = False

    def scroll_y(self):
        player = self.player.sprite
        player_y = player.rect.centery
        direction_y = player.direction.y

        if player_y < screen_height / 3 and direction_y < 0:
            self.world_shift = 16
            player.gravity = 2
            player.jump_speed = -16
            player.speed = 0
        elif player_y < screen_height / 6 and direction_y < 0:
            self.world_shift = 40
            player.gravity = 3
            player.jump_speed = -16
            player.speed = 0
        elif player_y > screen_height - (screen_height / 3) and direction_y > 0:
            self.world_shift = -4
            player.gravity = 0.2
            player.jump_speed = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.gravity = 0.8
            player.jump_speed = -16
            player.speed = 8

    def get_player_on_ground(self):
        if self.player.sprite.on_ground:
            self.player_on_ground = True
        else:
            self.player_on_ground = False

    def create_landing_dust(self):
        if not self.player_on_ground and self.player.sprite.on_ground and not self.dust_sprite.sprites():
            if self.player.sprite.facing_right:
                offset = pygame.math.Vector2(10, 15)
            else:
                offset = pygame.math.Vector2(-10, 15)
                fall_dust_particle = ParticleEffect(
                    self.player.sprite.rect.midbottom - offset, 'land')
                self.dust_sprite.add(fall_dust_particle)

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

        # enemy
        self.enemy_sprites.update(self.world_shift)
        self.constraint_sprites.update(self.world_shift)
        self.enemy_collision_reverse()
        self.enemy_sprites.draw(self.display_surface)

        # dust sprites
        self.dust_sprite.update(self.world_shift)
        self.dust_sprite.draw(self.display_surface)

        # player sprites
        self.player.update()
        self.horizontal_movement_collision()
        self.get_player_on_ground()
        self.vertical_movement_collision()
        self.create_landing_dust()
        self.scroll_y()
        self.player.draw(self.display_surface)
        self.goal.update(self.world_shift)
        self.goal.draw(self.display_surface)
