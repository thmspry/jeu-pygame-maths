from pygame.sprite import Group

from Enemy import *
from Player import *
from Projectile import ProjectileEnemy
from plateforme import Plateforme
from Move import *


class GameState:
    def __init__(self):
        self.player = Player(20, self)
        self.enemy = Enemy(700)
        self.platforms = [
            pygame.Rect(0, 450, 300, 50), pygame.Rect(800, 450, 300, 50),
            pygame.Rect(400, 300, 300, 50)
        ]
        self.platforms_group = Group()
        for plateform_rect in self.platforms:
            plateform = Plateforme(plateform_rect)
            self.platforms_group.add(plateform)
        self.projectiles_group = Group()
        self.delay = 0
        self.delay_IA = 0
        self.after_jump_IA = False
        self.decalage_droite_IA = False
        self.decalage_gauche_IA = False
        self.projectile_enemy_group = Group()

    def draw(self, window):
        window.blit(GameConfig.Background_IMG, (0, 0))
        self.player.draw(window)
        self.enemy.draw(window)
        for plateforme in self.platforms_group:
            pygame.draw.rect(window, (0, 255, 0), plateforme)
        if self.player.a_tire and self.player.delay >= 20:
            projectile = Projectile(self.player.rect.x + 20, self.player.rect.y, [GameConfig.ROCK_W, GameConfig.ROCK_H], self.player.direction)
            self.projectiles_group.add(projectile)
            self.player.a_tire = False
        for projectile in self.projectiles_group:
            projectile.mouvement(20)
            if projectile.rect.top >= GameConfig.Y_GROUND:
                self.projectiles_group.remove(projectile)
            if self.enemy.rect.colliderect(projectile.rect):
                self.enemy.get_hit(10, 0, 0)
                self.projectiles_group.remove(projectile)
                self.enemy.rect.x += 3

        for projectile in self.projectiles_group:
            projectile.draw(window)

        '''if self.enemy.a_tire:
            projectile_enemy = ProjectileEnemy(self.enemy.rect.x +20, self.enemy.rect.y-10, 20, (random.random(), random.random()))
            self.projectile_enemy_group.add(projectile_enemy)
            self.enemy.a_tire = False
        for projectile in self.projectile_enemy_group:
            projectile.mouvement()
            if self.player.rect.colliderect(projectile.rect):
                self.player.get_hit(10, 0, 0)
                self.projectile_enemy_group.remove(projectile)
                self.player.rect.x += 3
                self.enemy.nb_tir-=1

        for projectile in self.projectile_enemy_group:
            projectile.draw(window)'''



    def is_win(self):
        return self.player.life > 0 and self.enemy.life <= 0

    def is_lose(self):
        return self.player.life <= 0 and self.enemy.life > 0

    def advance_state(self, next_move):
        self.player.advance_state(next_move, self.enemy)
        #self.player.IA(self.enemy)
        self.enemy.advance_state(next_move, self.player)

    def parabole(self, x, decalage):
        return 0.07 * (x ** 2) + 3 * x -decalage

    def get_ia_command(self):
        next_move = Move()
        if self.player.rect.colliderect(self.enemy.rect):
            if self.delay_IA >= 70:
                next_move.up = True
                self.after_jump_IA = True
                self.delay_IA = 0
            else:
                self.delay_IA += 1
                if random.randint(0, 1) == 0:
                    next_move.punch = True
                else:
                    next_move.punch_foot = True
        else:
            delta_x = self.player.rect.x - self.enemy.rect.x
            if not self.after_jump_IA:
                if (-450 < delta_x < -300 and self.player.direction == Player.RIGHT) or (300 < delta_x < 450 and self.player.direction == Player.LEFT):
                    next_move.tir = True
                if delta_x < -450 or (0 < delta_x < 300):
                    next_move.right = True
                if (0 > delta_x > -300) or delta_x > 450:
                    next_move.left = True
            else:
                if self.player.touch_border_left() or self.decalage_droite_IA:
                    next_move.right = True
                    self.decalage_droite_IA = True
                if self.player.touch_border_right() or self.decalage_gauche_IA:
                    next_move.left = True
                    self.decalage_gauche_IA = True
                if abs(delta_x > 500):
                    self.after_jump_IA = False
                    self.decalage_gauche_IA = False
                    self.decalage_droite_IA = False

        print(self.decalage_gauche_IA, " ; ", self.decalage_droite_IA, " ; ", self.after_jump_IA)


        '''if self.after_jump_IA:
                    if self.player.rect.x < self.enemy.rect.x:
                        if not self.player.touch_border():
                            next_move.right = True
                        else:
                            self.after_jump_IA = False
                    else:
                        if not self.player.touch_border():
                            next_move.left = True
                        else:
                            self.after_jump_IA = False'''

        '''result_y = self.parabole(self.enemy.rect.x, 36400.0)
        print(result_y)
        if result_y < GameConfig.Y_GROUND:
            next_move.right = True
        if result_y > GameConfig.Y_GROUND:
            next_move.left = True
        if result_y == GameConfig.Y_GROUND:
            next_move.tir = True'''
        return next_move
