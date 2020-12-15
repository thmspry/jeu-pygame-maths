import pygame
from Player import *

class GameState:
    def __init__(self):
        self.player = Player(20)

    def draw(self, window):
        window.blit(GameConfig.Background_IMG, (0, 0))
        self.player.draw(window)

    def advance_state(self, next_move):
        self.player.advance_state(next_move)
