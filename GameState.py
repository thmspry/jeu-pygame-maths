from pygame.sprite import Group

from Enemy import *
from Player import *
from Projectile import ProjectileEnemy
from plateforme import Plateforme
from Move import *


class GameState:
    def __init__(self):
        self.player = Player(20, self)  # On a un personnage
        self.enemy = Enemy(700)  # Un ennemi
        self.platforms = [
            pygame.Rect(0, 450, 300, 50), pygame.Rect(800, 450, 300, 50),
            pygame.Rect(400, 300, 300, 50)
        ]  # Trois plateformes
        self.platforms_group = Group()
        for plateform_rect in self.platforms:  # Forme de la plateforme
            plateform = Plateforme(plateform_rect)
            self.platforms_group.add(plateform)
        self.projectiles_group = Group()  # On a plusieurs projectile pour le joueur
        self.projectile_enemy_group = Group()  # et pour l'ennemi
        # Variables utililes pour l'exeperience utilisateur
        self.delay = 0
        self.delay_IA = 0
        self.after_jump_IA = False
        self.decalage_droite_IA = False
        self.decalage_gauche_IA = False

    def draw(self, window):
        # Elements principaux
        window.blit(GameConfig.Background_IMG, (0, 0))
        self.player.draw(window)
        self.enemy.draw(window)
        for plateforme in self.platforms_group:
            pygame.draw.rect(window, (0, 255, 0), plateforme)

        # Projectiles
        # Joueur
        if self.player.a_tire and self.player.delay >= 20:  # Si le joueur tire et que le temps entre ce tir et le précédent est correct
            projectile = Projectile(self.player.rect.x + 20, self.player.rect.y, [GameConfig.ROCK_W, GameConfig.ROCK_H],
                                    self.player.direction)  # On créer un projectile
            self.projectiles_group.add(projectile)  # On l'ajoute au group
            self.player.a_tire = False  # Le joueur ne tire plus
        for projectile in self.projectiles_group:  # Pour tous les projectiles
            projectile.mouvement(20)  # On fait avancer le mouvement du projectile (valeur de 20 car plutôt réaliste)
            if projectile.rect.top >= GameConfig.Y_GROUND:  # Si le projectile touche le sol
                self.projectiles_group.remove(projectile)  # Il est détruit
            if self.enemy.rect.colliderect(projectile.rect):  # S'il touche l'ennemi
                self.enemy.get_hit(10, 0, 0)  # L'ennemi se prends un dégat
                self.projectiles_group.remove(projectile)  # Le projectile est détruit
                self.enemy.rect.x += 3  # L'ennemi bouge un petit peu pour simuler un choc

        for projectile in self.projectiles_group:  # Pour tous les projectiles
            projectile.draw(window)  # On les dessines

            # Ennemi
        if self.enemy.a_tire:  # Si l'ennemi tire
            projectile_enemy = ProjectileEnemy(self.enemy.rect.x + 20, self.enemy.rect.y - 10, 20,
                                               (random.random(), random.random()))  # On créer un projectile
            self.projectile_enemy_group.add(projectile_enemy)  # On l'ajoute au group
            self.enemy.a_tire = False  # L'ennemi ne tire plus
        for projectile in self.projectile_enemy_group:  # Pour tous les projectiles
            projectile.mouvement()  # On fait avancer le mouvement du projectile
            if self.player.rect.colliderect(projectile.rect):  # Si le projectile touche le joueur
                self.player.get_hit(10, 0, 0)  # Le joueur se prends un dégat
                self.projectile_enemy_group.remove(projectile)  # Il est détruit
                self.player.rect.x += 3  # Le joueur bouche pour simuler un choc
                self.enemy.nb_tir -= 1  # Le nombre de projectile iré décrémente

        for projectile in self.projectile_enemy_group:  # Pour tous les projectiles
            projectile.draw(window)  # On les dessines

    def is_win(self):  # Gagné si le joueur et toujours en vie et l'ennemi non
        return self.player.life > 0 and self.enemy.life <= 0

    def is_lose(self):  # Perdu si le joueur est mort et l'ennemi toujours en vie
        return self.player.life <= 0 and self.enemy.life > 0

    def advance_state(self, next_move):  # On fait avancer l'état de la partie
        self.player.advance_state(next_move, self.enemy)
        self.enemy.advance_state(next_move, self.player)

    def get_ia_command(self):  # Foncion de l'IA
        next_move = Move()  # On répure les mouvements possibles
        if self.player.rect.colliderect(self.enemy.rect):  # Si le joueur est en colision avec l'ennemi (cas bagare)
            if self.delay_IA < 70:  # Si le delai avant de sauter n'est pas encore bon
                self.delay_IA += 1  # Le délai augmente (le temps passe)
                if random.randint(0, 1) == 0:  # On choisi un coup au hasard grace a un int
                    next_move.punch = True  # Soit un coup de poing
                else:
                    next_move.punch_foot = True  # Soit un coup de pied
            else:  # Si le joueur a passer assez de temps a taper l'ennemi (cas début fuite)
                next_move.up = True  # Il saute
                self.after_jump_IA = True  # variable utile dans la seconde partie de l'IA
                self.delay_IA = 0
        else:  # Sinon, le joueur n'est pas en colision avec l'ennemi (cas régulier)
            delta_x = self.player.rect.x - self.enemy.rect.x  # On calcule l'ecart de position en X entre les deux
            if self.after_jump_IA:  # Si on a réaliser un saut juste avant (suite du cas de fuite)
                if self.player.touch_border_left() or self.decalage_droite_IA:
                    # Si on est contre le bord gauche (on vient de faire le saut) ou qu'on est entrain de se decaler
                    next_move.right = True  # On va a droite pour s'éloigner de l'ennemi
                    self.decalage_droite_IA = True  # On commence donc le décalage
                if self.player.touch_border_right() or self.decalage_gauche_IA:
                    # Si on est contre le bord droit (on vient de faire le saut) ou qu'on est entrain de se decaler
                    next_move.left = True  # On va a gauche pour s'éloigner de l'ennemi
                    self.decalage_gauche_IA = True  # On commence donc le décalage
                if abs(delta_x > 500):  # Si le décalage est assez suffisant pour reprendre en cycle normal
                    self.after_jump_IA = False  # On est plus dans le cas particulier du saut + decalage
                    self.decalage_gauche_IA = False
                    self.decalage_droite_IA = False
            else:  # On est dans le cas régulier ou le perso tire des pierre
                if (-450 < delta_x < -300 and self.player.direction == Player.RIGHT) or (
                        300 < delta_x < 450 and self.player.direction == Player.LEFT):
                    # Il tire dans le cas ou l'impact est a bonne distance pour touche l'ennemi et qu'il est dans la bonne direction
                    next_move.tir = True
                if delta_x <= -450 or (0 < delta_x < 300):  # S'il est trop loin (J a gauche, E a droite) ou trop proche (J:D, E:G)
                    next_move.right = True                  # Se rapproche ou s'éloine suivant la situation
                if (0 > delta_x > -300) or delta_x > 450:   # S'il est trop proche (J:G, E:D) ou trop loin (J:D, E:G)
                    next_move.left = True                   # Se rapproche ou s'éloine suivant la situation

        # Tentative de l'utilisation de la fonction du lancer pour determiner le moment du lancer
        '''result_y = self.parabole(self.enemy.rect.x, 36400.0)
        print(result_y)
        if result_y < GameConfig.Y_GROUND:
            next_move.right = True
        if result_y > GameConfig.Y_GROUND:
            next_move.left = True
        if result_y == GameConfig.Y_GROUND:
            next_move.tir = True'''
        return next_move
