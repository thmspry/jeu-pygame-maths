import pygame
from config import *
from Player import *
from  GameState import *


class Move:
    def __init__(self):
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.attack = False

def get_next_move():
    next_move = Move()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        next_move.right = True
    if keys[pygame.K_LEFT]:
        next_move.left = True
    if keys[pygame.K_UP]:
        next_move.up = True
    if keys[pygame.K_SPACE]:
        next_move.attack = True
    return next_move


def Gameloop(window):
    gameState = GameState()
    quitting = False
    while not quitting:
        pygame.time.delay(20)
        gameState.draw(window)
        next_move = get_next_move()
        gameState.advance_state(next_move)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitting = True
        pygame.display.update()


pygame.init()
Player.init_sprites()
Enemy.init_sprites()
window = pygame.display.set_mode((GameConfig.windowW, GameConfig.windowH))
Gameloop(window)
pygame.quit()
quit()
