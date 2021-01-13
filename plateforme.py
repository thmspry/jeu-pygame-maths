import pygame


class Plateforme(pygame.sprite.Sprite):

    def __init__(self, rect):
        super().__init__()
        self.rect = rect

    def afficher(self, surface):        # Une plateforme est un rectangle vert
        pygame.draw.rect(surface, (0, 155, 0), self.rect)
