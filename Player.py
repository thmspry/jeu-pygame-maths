import random
from config import *


class Player(pygame.sprite.Sprite):
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

    def __init__(self, x):
        self.rect = pygame.Rect(x, GameConfig.Y_GROUND - GameConfig.Player_H, GameConfig.Player_W,
                                GameConfig.Player_H)
        self.vx = 0
        self.vy = 0
        self.life = 100
        self.sprite_count = 0
        self.direction = Player.NONE
        self.image = Player.IMAGES[self.direction][self.sprite_count // GameConfig.NB_FRAMES_PER_SPRITE_PLAYER]
        self.mask = Player.MASK[self.direction][self.sprite_count // GameConfig.NB_FRAMES_PER_SPRITE_PLAYER]
        self.tmp = 0

    @staticmethod
    def init_sprites():
        Player.IMAGES = {Player.RIGHT: GameConfig.WALK_RIGHT_IMG, Player.NONE: GameConfig.STANDING_IMG,
                         Player.LEFT: GameConfig.WALK_LEFT_IMG, Player.UPL: GameConfig.JUMP_LEFT_IMG,
                         Player.UPR: GameConfig.JUMP_RIGHT_IMG, Player.PUNCH_LEFT : GameConfig.PUNCH_LEFT_IMG, Player.PUNCH_RIGHT : GameConfig.PUNCH_RIGHT_IMG,
                         Player.PUNCH_FOOT_RIGHT : GameConfig.PUNCH_FOOT_RIGHT_IMG, Player.PUNCH_FOOT_LEFT : GameConfig.PUNCH_FOOT_LEFT_IMG}
        Player.MASK = {Player.RIGHT: GameConfig.WALK_RIGHT_MASK, Player.NONE: GameConfig.STANDING_MASK,
                       Player.LEFT: GameConfig.WALK_LEFT_MASK, Player.UPR: GameConfig.JUMP_RIGHT_MASK, Player.PUNCH_LEFT : GameConfig.PUNCH_LEFT_MASK, Player.PUNCH_RIGHT : GameConfig.PUNCH_RIGHT_MASK,
                       Player.PUNCH_FOOT_RIGHT : GameConfig.PUNCH_FOOT_RIGHT_MASK, Player.PUNCH_FOOT_LEFT : GameConfig.PUNCH_FOOT_LEFT_MASK}

    def draw(self, window):
        window.blit(self.image, self.rect.topleft)
        pygame.draw.rect(window, GameConfig.GREY_BAR, pygame.Rect(175, 25, 200, 30))
        if self.life >= 0 :
            pygame.draw.rect(window, GameConfig.RED_LIFE, pygame.Rect(175, 25, self.life*2, 30))
        else:
            pygame.draw.rect(window, GameConfig.RED_LIFE, pygame.Rect(175, 25, 0, 30))

        img = GameConfig.FONT20.render("Life : " + str(self.life), True, GameConfig.WHITE)
        window.blit(img, (220, 57))

    def punch(self, enemy):
        rect = self.rect.copy()
        rect.inflate_ip(15, 0)
        if rect.colliderect(enemy.rect):
            enemy.get_hit(15)

    def punch_foot(self, enemy):
        rect = self.rect.copy()
        rect.inflate_ip(25, 0)
        if rect.colliderect(enemy.rect):
            enemy.get_hit(20)

    def shoot(self):
         pass

    def on_ground(self):
        return self.rect.bottom == GameConfig.Y_GROUND

    def on_platform(self):
        return self.rect.bottom <= GameConfig.Y_PLATFORMS[0] and self.rect.bottom <= GameConfig.Y_PLATFORMS[0] and self.rect.right >= GameConfig.X_PLATFORMS[0] and self.rect.left <= GameConfig.X_PLATFORMS[0] + GameConfig.PLATFORM_W

    def touch_border(self):
        return self.rect.right >= GameConfig.windowW or self.rect.left == 0 or self.rect.top <= 0

    def touch_enemy(self, enemy):
        return self.rect.colliderect(enemy.rect)

    def advance_state(self, next_move, enemy):
        fx = 0
        fy = 0
        print(self.rect.bottom, " ; ", GameConfig.Y_PLATFORMS[0])
        if next_move.left:
            fx = GameConfig.force_left_player
            self.direction = Player.LEFT
        elif next_move.right:
            fx = GameConfig.force_right_player
            self.direction = Player.RIGHT
        elif next_move.up:
            fy = GameConfig.FORCEJUMP
            self.direction = Player.UPR
        elif next_move.punch:
            self.punch(enemy)
            if self.direction == Player.LEFT:
                self.direction = Player.PUNCH_LEFT
            else:
                self.direction = Player.PUNCH_RIGHT
        elif next_move.punch_foot:
            self.punch(enemy)
            if self.direction == Player.LEFT:
                self.direction = Player.PUNCH_FOOT_LEFT
            else:
                self.direction = Player.PUNCH_FOOT_RIGHT
        else:
            self.direction = Player.NONE

        if self.touch_enemy(enemy):
            if self.tmp == 10:
                damage = random.randint(5,30)
                self.life = self.life - damage
                self.tmp = 0
            self.tmp +=1

        if self.life < 0:
            self.life=0

        self.sprite_count += 1
        if self.sprite_count >= GameConfig.NB_FRAMES_PER_SPRITE_PLAYER * len(Player.IMAGES[self.direction]):
            self.sprite_count = 0
        if not self.touch_border():
            self.image = Player.IMAGES[self.direction][
                self.sprite_count // GameConfig.NB_FRAMES_PER_SPRITE_PLAYER
                ]
        else:
            self.image = Player.IMAGES[Player.NONE][0]

        self.mask = Player.MASK[self.direction][self.sprite_count // GameConfig.NB_FRAMES_PER_SPRITE_PLAYER]

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
