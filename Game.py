import pygame
from config import *


class Move:
    def __init__(self):
        self.left = False
        self.right = False


class Player(pygame.sprite.Sprite):
    MASK = {}
    IMAGES = {}
    LEFT = -1
    RIGHT = 1
    NONE = 0

    def __init__(self, x):
        self.rect = pygame.Rect(x, GameConfig.Y_Platform - GameConfig.Player_H, GameConfig.Player_W,
                                GameConfig.Player_H)
        self.vx = 0
        self.vy = 0
        self.sprite_count = 0
        self.direction = Player.NONE
        self.image = Player.IMAGES[self.direction][self.sprite_count // GameConfig.NB_FRAMES_PER_SPRITE_PLAYER]
        self.mask = Player.MASK[self.direction][self.sprite_count // GameConfig.NB_FRAMES_PER_SPRITE_PLAYER]

    @staticmethod
    def init_sprites():
        Player.IMAGES = {Player.RIGHT: GameConfig.WALK_RIGHT_IMG, Player.NONE: GameConfig.STANDING_IMG}
        Player.MASK = {Player.RIGHT: GameConfig.WALK_RIGHT_MASK, Player.NONE: GameConfig.STANDING_MASK}

    def draw(self):
        window.blit(self.image, self.rect.topleft)

    def shoot(self):
        pass

    def advance_state(self, next_move):
        fx = 0
        fy = 0
        if next_move.left:
            fx = GameConfig.force_left_player
            self.direction = Player.LEFT
        if next_move.right:
            fx = GameConfig.force_right_player
            self.direction = Player.RIGHT
        else:
            self.direction = Player.NONE
        self.sprite_count += 1
        if self.sprite_count >= GameConfig.NB_FRAMES_PER_SPRITE_PLAYER * len(Player.IMAGES[self.direction]):
            print('aa')
            self.sprite_count = 0
        self.image = Player.IMAGES[self.direction][
            self.sprite_count // GameConfig.NB_FRAMES_PER_SPRITE_PLAYER
            ]
        self.mask = Player.MASK[self.direction][self.sprite_count // GameConfig.NB_FRAMES_PER_SPRITE_PLAYER]
        self.vx = fx * GameConfig.DT
        self.vy += fy * GameConfig.DT
        self.rect = self.rect.move(self.vx * GameConfig.DT, self.vy * GameConfig.DT)


class GameState:
    def __init__(self):
        self.player = Player(20)

    def draw(self, window):
        window.blit(GameConfig.Background_IMG, (0, 0))
        self.player.draw()

    def advance_state(self, next_move):
        self.player.advance_state(next_move)


def get_next_move():
    next_move = Move()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        next_move.right = True
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
window = pygame.display.set_mode((GameConfig.windowW, GameConfig.windowH))
Gameloop(window)
pygame.quit()
quit()
