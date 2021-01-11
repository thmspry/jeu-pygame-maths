import pygame
import random

from pygame.sprite import Group

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
        self.delay = 0
        self.a_tire = False
        self.tire_autorisee = 3
        self.direction_tir = 1
        self.delay_proj = 0
        self.nb_tir = 0

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

    def get_hit(self, attack, delay, limit):
        if delay == limit:
            self.life -= attack

    def on_ground(self):
        return self.rect.bottom == GameConfig.Y_GROUND

    def touch_border(self):
        return self.rect.right >= GameConfig.windowW or self.rect.left == 0 or self.rect.top <= 0 or self.rect.bottom >= GameConfig.windowH

    def advance_state(self, next_move, player):
        self_x = self.rect.left
        self_y = self.rect.top

        player_x = player.rect.left
        player_y = player.rect.top

        '''if next_move.punch  and player.touch_enemy(self):
            damage = random.randint(5,30)
            self.life = self.life - damage
        '''
        self.delay_proj+=1

        if self.delay_proj >= 30 and self.nb_tir<self.tire_autorisee:
            self.a_tire = True
            self.delay_proj = 0
            self.nb_tir+=1

        if player.touch_enemy(self):
            self.delay += 1
            damage = random.randint(5, 30)
            limit = 30
            player.get_hit(damage, self.delay, limit)
            if self.delay == limit:
                self.delay = 0

        if self.life < 0:
            self.life=0

        delta_x = player_x - self_x
        if delta_x > 0 :
            self.direction = Enemy.RIGHT
        else:
            self.direction = Enemy.LEFT
        self.image = Enemy.IMAGES[self.direction]
        if self.direction == Enemy.RIGHT:
            self.rect = self.rect.move(3, 0)
        else:
            self.rect = self.rect.move(-3, 0)

        '''Fonction affine
        denom = self_x - player_x
        if denom == 0:
            a = 10000000
        else:
            a = (self_y - player_y) / denom
        b = self_y / (a * self_x)
        print("Fonction : ", a, "X + ", b)
        self.rect = self.rect.move(GameConfig.FORCE_ENEMY * b, 0)'''



