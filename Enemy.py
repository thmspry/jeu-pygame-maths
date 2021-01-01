import pygame
from config import *


class Enemy(pygame.sprite.Sprite):
    IMAGES = {}
    LEFT = -1
    RIGHT = 1
    NONE = 0

    def __init__(self, x):
        self.rect = pygame.Rect(x, GameConfig.ENEMY_W, GameConfig.ENEMY_W,
                                GameConfig.ENEMY_H)
        self.vx = 0
        self.vy = 0
        self.direction = Enemy.NONE
        self.image = Enemy.IMAGES[self.direction]
        self.mask = GameConfig.ENEMY_MASK

    @staticmethod
    def init_sprites():
        Enemy.IMAGES = {Enemy.LEFT: GameConfig.ENEMY_LEFT_IMG,
                        Enemy.NONE: GameConfig.ENEMY_LEFT_IMG,
                        Enemy.RIGHT: GameConfig.ENEMY_RIGHT_IMG}

    def draw(self, window):
        window.blit(self.image, self.rect.topleft)

    def on_ground(self):
        if self.rect.bottom == GameConfig.Y_Platform:
            return True
        else:
            return False

    def touch_border(self):
        return self.rect.right >= GameConfig.windowW or self.rect.left == 0 or self.rect.top <= 0 or self.rect.bottom >= GameConfig.windowH

    def advance_state(self, player_x, player_y):
        self_x = self.rect.left
        self_y = self.rect.top

        # Fonction affine
        denom = self_x - player_x
        if denom == 0:
            a = 10000000
        else:
            a = (self_y - player_y) / denom
        b = self_y / (a * self_x)
        print("Fonction : ", a, "X + ", b)
        self.rect = self.rect.move(GameConfig.FORCE_ENEMY * b, 0)



