import math

import pygame
from config import *


class Projectile(pygame.sprite.Sprite):
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
        self.rebondD = False

    def draw(self, window):
        window.blit(self.image, self.rect)

    def mouvement(self, vitesse):
        if self.rebondD:
            self.rect.x -= vitesse * self.direction
        else:
            self.rect.x += vitesse * self.direction
        if self.lastY is not None and self.lastY > self.fonction_carre(self.pos):  # Si on est sur la montée
            self.rect.y -= self.fonction_carre(self.pos)
        else:
            self.rect.y += self.fonction_carre(self.pos)                           # Si on est sur la descente
        self.lastY = self.fonction_carre(self.pos)              # Utilisation de la fonction
        self.pos += 1                                           # On avance la position en X
        if self.rect.x >= GameConfig.windowW or self.rect.x <= 0:   # Si on touche le bord
            self.rebondD = True                                     # il y a un donc un rebond
        self.delay += 1
        if self.delay == 3:
            self.image = pygame.transform.rotate(self.image, -90)  # On fait tourner la pierre sur elle meme
            self.delay = 0

    def fonction_carre(self, x):        # Fonction modélisant la trajectoire de la parabole du lancer
        return 0.07 * (x ** 2) + 3 * x


class ProjectileEnemy(pygame.sprite.Sprite):

    def __init__(self, x, y, vitesse, direction):
        super().__init__()
        self.pos = pygame.math.Vector2((x, y))
        self.vitesse = vitesse
        self.dir = pygame.math.Vector2(direction).normalize()
        self.image = GameConfig.ROCK_IMG
        self.rect = self.image.get_rect(center=(round(self.pos.x), round(self.pos.y)))

    def draw(self, window):
        window.blit(self.image, self.rect)

    def reflect(self, NV):
        self.dir = self.dir.reflect(pygame.math.Vector2(NV))

    def mouvement(self): # Pierre rebondisant a 90 sur tout l'écran
        self.pos += self.dir * self.vitesse
        self.rect.center = round(self.pos.x), round(self.pos.y)
        if self.rect.left <= 0:
            self.reflect((1, 0))
        if self.rect.right >= GameConfig.windowW:
            self.reflect((-1, 0))
        if self.rect.top <= 0:
            self.reflect((0, 1))
        if self.rect.bottom >= GameConfig.windowH - 100:
            self.reflect((0, -1))
