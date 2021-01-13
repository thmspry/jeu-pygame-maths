import random

from Projectile import Projectile
from config import *


class Player(pygame.sprite.Sprite):
    # Sprites et mouvements
    MASK = {}
    IMAGES = {}
    LEFT = -1
    RIGHT = 1
    UPL = 2
    UPR = 3
    PUNCH_LEFT = 4
    PUNCH_RIGHT = 5
    PUNCH_FOOT_LEFT = 6
    PUNCH_FOOT_RIGHT = 7
    DOWN = -2
    NONE = 0


    def __init__(self, x, gameState):
        self.rect = pygame.Rect(x, GameConfig.Y_GROUND - GameConfig.Player_H, GameConfig.Player_W,
                                GameConfig.Player_H)
        self.vx = 0
        self.vy = 0
        self.fx = 0
        self.fy = 0
        self.life = 100
        self.sprite_count = 0
        self.direction = Player.NONE
        self.image = Player.IMAGES[self.direction][self.sprite_count // GameConfig.NB_FRAMES_PER_SPRITE_PLAYER]
        self.mask = Player.MASK[self.direction][self.sprite_count // GameConfig.NB_FRAMES_PER_SPRITE_PLAYER]
        self.delay = 19
        self.gameState = gameState

        self.a_tire = False
        self.tire_autorisee = 2
        self.direction_tir = 1


    @staticmethod
    def init_sprites():
        # Tableaux qui associent la direction avec un tableau de sprite
        Player.IMAGES = {Player.RIGHT: GameConfig.WALK_RIGHT_IMG, Player.NONE: GameConfig.STANDING_IMG,
                         Player.LEFT: GameConfig.WALK_LEFT_IMG, Player.UPL: GameConfig.JUMP_LEFT_IMG,
                         Player.UPR: GameConfig.JUMP_RIGHT_IMG, Player.PUNCH_LEFT : GameConfig.PUNCH_LEFT_IMG, Player.PUNCH_RIGHT : GameConfig.PUNCH_RIGHT_IMG,
                         Player.PUNCH_FOOT_RIGHT : GameConfig.PUNCH_FOOT_RIGHT_IMG, Player.PUNCH_FOOT_LEFT : GameConfig.PUNCH_FOOT_LEFT_IMG}
        Player.MASK = {Player.RIGHT: GameConfig.WALK_RIGHT_MASK, Player.NONE: GameConfig.STANDING_MASK,
                       Player.LEFT: GameConfig.WALK_LEFT_MASK, Player.UPR: GameConfig.JUMP_RIGHT_MASK, Player.PUNCH_LEFT : GameConfig.PUNCH_LEFT_MASK, Player.PUNCH_RIGHT : GameConfig.PUNCH_RIGHT_MASK,
                       Player.PUNCH_FOOT_RIGHT : GameConfig.PUNCH_FOOT_RIGHT_MASK, Player.PUNCH_FOOT_LEFT : GameConfig.PUNCH_FOOT_LEFT_MASK}

    def draw(self, window):
        window.blit(self.image, self.rect.topleft)
        # On associe au personnage sa barre de vie
        pygame.draw.rect(window, GameConfig.GREY_BAR, pygame.Rect(175, 25, 200, 30))  # Fond de la barre de vie
        if self.life >= 0:
            pygame.draw.rect(window, GameConfig.RED_LIFE, pygame.Rect(175, 25, self.life*2, 30)) # Modélisé par un rect de largeur vie*2

        img = GameConfig.FONT20.render("Life : " + str(self.life), True, GameConfig.WHITE)  # Texte "Life"
        window.blit(img, (220, 57))

    def punch(self, enemy, delay):  # Coup de poing
        rect = self.rect.copy()
        rect.inflate_ip(15, 0)      # Grandi la hitbox
        limit = 20                  # Limite du delai
        if rect.colliderect(enemy.rect):     # Si le player touche l'ennemi
            enemy.get_hit(15, delay, limit)  # L'ennemi se prend un dégat
            if self.delay >= limit:          # Si le délai atteint la limite
                self.delay = 0               # Le délai se rénitialise

    def punch_foot(self, enemy, delay):  # Coup de pied
        rect = self.rect.copy()
        rect.inflate_ip(25, 0)           # Grandi la hitbox
        limit = 26                       # Limite du delai
        if rect.colliderect(enemy.rect):    # Si le player touche l'ennemi
            enemy.get_hit(20, delay, limit)  # L'ennemi se prend un dégat
            if self.delay >= limit:          # Si le délai atteint la limite
                self.delay = 0               # Le délai se rénitialise

    def on_ground(self):  # Est sur le sol
        return self.rect.bottom == GameConfig.Y_GROUND

    def on_platform(self):  # Est sur un plateforme
        for plateform in self.gameState.platforms_group:    # Parmis les plateforme
            if self.rect.midbottom[1] // 10 * 10 == plateform.rect.top and self.rect.colliderect(plateform):
                # Si le bas du personnage est égal au haut de la plateforme et la touche
                return True

    def touch_border(self):     # S'il touche un des bords
        return self.touch_border_left() or self.touch_border_right()

    def touch_border_left(self):    # S'il touche le bord gauche
        return self.rect.left <= 0

    def touch_border_right(self):   # S'il touche le bord droit
        return self.rect.right >= GameConfig.windowW

    def touch_enemy(self, enemy):
        return self.rect.colliderect(enemy.rect)

    def get_hit(self, attack, delay, limit):    # Se prend un dégat
        if delay == limit:
            self.life -= attack

    def advance_state(self, next_move, enemy):
        fx = 0
        fy = 0
        # Suivant la direction, la force et direction se met a jour
        if next_move.left:
            fx = GameConfig.force_left_player
            self.direction = Player.LEFT
        elif next_move.right:
            fx = GameConfig.force_right_player
            self.direction = Player.RIGHT
        elif next_move.up:
            fy = GameConfig.FORCEJUMP
            self.direction = Player.UPR
        elif next_move.punch:   # Coup de poing
            self.delay += 1
            self.punch(enemy, self.delay)
            if self.direction == Player.LEFT:
                self.direction = Player.PUNCH_LEFT
            else:
                self.direction = Player.PUNCH_RIGHT
        elif next_move.punch_foot:
            self.delay += 1
            self.punch_foot(enemy, self.delay)
            if self.direction == Player.LEFT:
                self.direction = Player.PUNCH_FOOT_LEFT
            else:
                self.direction = Player.PUNCH_FOOT_RIGHT
        elif next_move.tir:
            self.delay += 1
            self.a_tire = True
            if self.delay > 20:
                self.delay = 0
        else:
            self.delay = 19

        if self.life < 0:  # Pour éviter le débordement
            self.life = 0

        self.sprite_count += 1  # Pour faire tourner l'animation
        if self.sprite_count >= GameConfig.NB_FRAMES_PER_SPRITE_PLAYER * len(Player.IMAGES[self.direction]):
            self.sprite_count = 0   # On arrive au bout de l'animation, on retourne au début
        if not self.touch_border(): # On fait tourner l'animation si on touche pas le bord
            self.image = Player.IMAGES[self.direction][
                self.sprite_count // GameConfig.NB_FRAMES_PER_SPRITE_PLAYER
                ]
        else:
            self.image = Player.IMAGES[Player.NONE][0]

        # Met a jour le mask
        self.mask = Player.MASK[self.direction][self.sprite_count // GameConfig.NB_FRAMES_PER_SPRITE_PLAYER]

        # Equation Newton
        self.vx = fx * GameConfig.DT
        if self.on_ground() or self.on_platform():
            self.vy = fy*GameConfig.DT
        else:
            self.vy = self.vy + GameConfig.GRAVITY*GameConfig.DT

        x, y = self.rect.topleft
        vy_max = (GameConfig.Y_GROUND-GameConfig.Player_H-y)/GameConfig.DT
        self.vy = min(self.vy, vy_max)
        vx_min = -x/GameConfig.DT
        vx_max = (GameConfig.windowW-GameConfig.Player_W-x)/GameConfig.DT
        self.vx = min(self.vx, vx_max)
        self.vx = max(self.vx, vx_min)
        self.rect = self.rect.move(self.vx * GameConfig.DT, self.vy * GameConfig.DT)