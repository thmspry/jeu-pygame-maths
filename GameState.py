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
        pygame.draw.rect(window, GameConfig.RED_LIFE, pygame.Rect(GameConfig.X_PLATFORMS[0], GameConfig.Y_PLATFORMS[0], GameConfig.PLATFORM_W, 30))

    def is_win(self):
        return self.player.life > 0 and self.enemy.life <= 0

    def is_lose(self):
        return self.player.life <= 0 and self.enemy.life > 0


    def advance_state(self, next_move):
        self.player.advance_state(next_move, self.enemy)
        self.enemy.advance_state(next_move, self.player)


