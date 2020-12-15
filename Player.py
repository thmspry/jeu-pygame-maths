import pygame
from config import *


class Player(pygame.sprite.Sprite):
    MASK = {}
    IMAGES = {}
    LEFT = -1
    RIGHT = 1
    UP = 2
    DOWN = -2
    NONE = 0

    def __init__(self, x):
        self.rect = pygame.Rect(x, GameConfig.Y_Platform - GameConfig.Player_H, GameConfig.Player_W,
                                GameConfig.Player_H)
        self.vx = 0
        self.vy = 0
        self.sprite_count = 0
        self.direction = Player.NONE
        self.image = Player.IMAGES[self.direction][self.sprite_count // GameConfig.NB_FRAMES_PER_SPRITE_PLAYER]
        self.mask = Player.MASK[self.direction][self.sprite_count // GameConfig.NB_FRAMES_PER_SPRITE_PLAYER]

    @staticmethod
    def init_sprites():
        Player.IMAGES = {Player.RIGHT: GameConfig.WALK_RIGHT_IMG, Player.NONE: GameConfig.STANDING_IMG,
                         Player.LEFT: GameConfig.WALK_LEFT_IMG}
        Player.MASK = {Player.RIGHT: GameConfig.WALK_RIGHT_MASK, Player.NONE: GameConfig.STANDING_MASK,
                       Player.LEFT: GameConfig.WALK_LEFT_IMG}

    def draw(self, window):
        print(self.direction)
        window.blit(self.image, self.rect.topleft)

    def shoot(self):
        pass

    def advance_state(self, next_move):
        fx = 0
        fy = 0
        if next_move.left:
            fx = GameConfig.force_left_player
            self.direction = Player.LEFT
        elif next_move.right:
            fx = GameConfig.force_right_player
            self.direction = Player.RIGHT
        else:
            self.direction = Player.NONE
        self.sprite_count += 1
        if self.sprite_count >= GameConfig.NB_FRAMES_PER_SPRITE_PLAYER * len(Player.IMAGES[self.direction]):
            self.sprite_count = 0
        self.image = Player.IMAGES[self.direction][
            self.sprite_count // GameConfig.NB_FRAMES_PER_SPRITE_PLAYER
            ]
        self.mask = Player.MASK[self.direction][self.sprite_count // GameConfig.NB_FRAMES_PER_SPRITE_PLAYER]
        self.vx = fx * GameConfig.DT
        self.vy += fy * GameConfig.DT
        self.rect = self.rect.move(self.vx * GameConfig.DT, self.vy * GameConfig.DT)