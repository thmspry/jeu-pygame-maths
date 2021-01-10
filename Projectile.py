import pygame
from config import *


class Projectile(pygame.sprite.Sprite) :
    def __init__(self, x, y, taille, direction):
        super().__init__()
        self.x = x
        self.y = y
        self.taille = taille
        self.direction = direction
        self.vy = 0
        self.image = GameConfig.ROCK_IMG
        self.rect = pygame.Rect(self.x, self.y, self.taille[0], self.taille[1])

    def draw(self, window):
        window.blit(self.image, self.rect)

    def mouvement(self, vitesse):
        self.rect.x += vitesse * self.direction
        self.image = pygame.transform.flip(self.image, True, False)
    '''def advance_state(self, next_move):
        if next_move.attack :
            self.vx = self.vx*GameConfig.DT
            self.draw()
'''