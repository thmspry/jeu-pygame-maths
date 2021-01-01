import pygame
from config import *
class Projectile(pygame.sprite.Sprite) :
    def __init__(self, x, y) :
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y,
            GameConfig.ROCK_W,
            GameConfig.ROCK_W)
        self.vx = 0
        self.vy = 0
        self.image = GameConfig.ROCK_IMG
        self.mask = GameConfig.ROCK_IMG_MASK

    def draw(self, window) :
            window.blit(self.image, self.rect.topleft)

    def advance_state(self, next_move) :
        if next_move.attack :
            self.vx = self.vx*GameConfig.DT
            self.draw()
