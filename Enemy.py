import pygame
import random
from config import *


class Enemy(pygame.sprite.Sprite):
    IMAGES = {}
    LEFT = -1
    RIGHT = 1
    NONE = 0

    def __init__(self, x):
        self.rect = pygame.Rect(x, 500 , GameConfig.ENEMY_W,
                                GameConfig.ENEMY_H)
        self.vx = 0
        self.vy = 0
        self.life = 100
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
        pygame.draw.rect(window, GameConfig.GREY_BAR, pygame.Rect(700, 25, 200, 30))
        if self.life >= 0:
            pygame.draw.rect(window, GameConfig.RED_LIFE, pygame.Rect(700, 25, self.life*2, 30))
        else:
            pygame.draw.rect(window, GameConfig.RED_LIFE, pygame.Rect(700, 25, 0, 30))

        img = GameConfig.FONT20.render("Life : " + str(self.life), True, GameConfig.WHITE)
        window.blit(img, (750, 57))

    def on_ground(self):
        return self.rect.bottom == GameConfig.Y_GROUND

    def touch_border(self):
        return self.rect.right >= GameConfig.windowW or self.rect.left == 0 or self.rect.top <= 0 or self.rect.bottom >= GameConfig.windowH

    def advance_state(self, next_move, player):
        self_x = self.rect.left
        self_y = self.rect.top

        player_x = player.rect.left
        player_y = player.rect.top

        if next_move.attack  and player.touch_enemy(self):
            damage = random.randint(5,30)
            self.life = self.life - damage

        if self.life < 0:
            self.life=0

        delta_x =  player_x - self_x
        if delta_x > 0 :
            self.direction = Enemy.RIGHT
        else:
            self.direction = Enemy.LEFT
        self.image = Enemy.IMAGES[self.direction]
        self.rect = self.rect.move(delta_x/50, 0)

        '''Fonction affine
        denom = self_x - player_x
        if denom == 0:
            a = 10000000
        else:
            a = (self_y - player_y) / denom
        b = self_y / (a * self_x)
        print("Fonction : ", a, "X + ", b)
        self.rect = self.rect.move(GameConfig.FORCE_ENEMY * b, 0)'''



