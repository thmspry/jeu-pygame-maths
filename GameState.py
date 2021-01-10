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
        self.projectiles_group = Group()

    def draw(self, window):
        window.blit(GameConfig.Background_IMG, (0, 0))
        self.player.draw(window)
        self.enemy.draw(window)
        for plateforme in self.platforms_group:
            pygame.draw.rect(window, (0, 255, 0), plateforme)

        if self.player.a_tire:
            projectile = Projectile(self.player.rect.x + 20, self.player.rect.y -10, [10, 10], self.player.direction)
            self.projectiles_group.add(projectile)
            self.player.a_tire = False
        for projectile in self.projectiles_group:
            projectile.mouvement(50)
            if projectile.rect.right >= window.get_width() or projectile.rect.left <= 0:
                self.projectiles_group.remove(projectile)
            if self.enemy.rect.colliderect(projectile.rect):
                self.enemy.get_hit(10, 0, 0)
                self.projectiles_group.remove(projectile)
                self.enemy.rect.x += 3

        for projectile in self.projectiles_group:
            projectile.draw(window)



    def is_win(self):
        return self.player.life > 0 and self.enemy.life <= 0

    def is_lose(self):
        return self.player.life <= 0 and self.enemy.life > 0

    def advance_state(self, next_move):
        self.player.advance_state(next_move, self.enemy)
        self.enemy.advance_state(next_move, self.player)
