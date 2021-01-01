import pygame
from Player import *
from Projectile import *
from Enemy import *

class GameState:
    def __init__(self):
        self.player = Player(20)
        self.enemy = Enemy(500)

    def draw(self, window):
        window.blit(GameConfig.Background_IMG, (0, 0))
        self.player.draw(window)
        self.enemy.draw(window)

    def is_over(self):
        return self.player.touch_enemy(self.enemy)


    def advance_state(self, next_move):
        self.player.advance_state(next_move)
        self.enemy.advance_state(self.player.rect.left, self.player.rect.top)


