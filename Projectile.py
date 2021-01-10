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
        self.delay = 0
        self.pos = -10
        self.lastY = None

    def draw(self, window):
        window.blit(self.image, self.rect)

    def mouvement(self, vitesse):
        self.rect.x += vitesse * self.direction
        if self.lastY is not None and self.lastY > self.fonction_carre(self.pos):
            self.rect.y -= self.fonction_carre(self.pos)
        else:
            self.rect.y += self.fonction_carre(self.pos)
        self.lastY = self.fonction_carre(self.pos)
        self.pos+=1

        print(self.rect.x, "       ", self.rect.y)
        self.delay += 1
        if self.delay == 3:
            self.image = pygame.transform.rotate(self.image, -90)
            self.delay = 0
    '''def advance_state(self, next_move):
        if next_move.attack :
            self.vx = self.vx*GameConfig.DT
            self.draw()
'''
    def fonction_carre(self, x):
        return (-1 * (x**2))+(1*x)+3
