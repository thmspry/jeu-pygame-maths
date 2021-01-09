from pygame.sprite import Group

from Enemy import *
from Player import *
from plateforme import Plateforme


class GameState:
    def __init__(self):
        self.player = Player(20, self)
        self.enemy = Enemy(500)
        self.platforms = [
            pygame.Rect(0, 450, 300, 50), pygame.Rect(800, 450, 300, 50),
            pygame.Rect(400, 300, 300, 50)
        ]
        self.platforms_group = Group()
        for plateform_rect in self.platforms:
            plateform = Plateforme(plateform_rect)
            self.platforms_group.add(plateform)

    def draw(self, window):
        window.blit(GameConfig.Background_IMG, (0, 0))
        self.player.draw(window)
        self.enemy.draw(window)
        for plateforme in self.platforms_group:
            pygame.draw.rect(window, (0, 255, 0), plateforme)


    def is_win(self):
        return self.player.life > 0 and self.enemy.life <= 0

    def is_lose(self):
        return self.player.life <= 0 and self.enemy.life > 0

    def advance_state(self, next_move):
        self.player.advance_state(next_move, self.enemy)
        self.enemy.advance_state(next_move, self.player)
