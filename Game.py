import pygame
from config import *
from Player import *
from GameState import *


class Move:
    def __init__(self):
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.punch = False
        self.punch_foot = False
        self.tir = False


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
    if keys[pygame.K_x]:
        next_move.punch = True
    if keys[pygame.K_c]:
        next_move.punch_foot = True
    if keys[pygame.K_w]:
        next_move.tir = True
    return next_move


def Gameloop(window):
    game_state = GameState()
    quitting = False
    while not quitting:
        pygame.time.delay(100)
        game_state.draw(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitting = True
        if game_state.is_win():
            display_message(window, "You WIN", GameConfig.FONT150, GameConfig.windowW / 2, GameConfig.windowH / 2 - 50, GameConfig.YELLOW_GOLD_WIN)
            display_message(window, "Press any key to continue", GameConfig.FONT20, GameConfig.windowW / 2,
                            GameConfig.windowH / 2 + 50, GameConfig.BLACK)
            quitting = True
        if game_state.is_lose():
            display_message(window, "You LOSE", GameConfig.FONT150, GameConfig.windowW / 2, GameConfig.windowH / 2 - 50,
                            GameConfig.RED_DARK_LOSE)
            display_message(window, "Press any key to continue", GameConfig.FONT20, GameConfig.windowW / 2,
                            GameConfig.windowH / 2 + 50, GameConfig.BLACK)
            quitting = True
        next_move = get_next_move()
        game_state.advance_state(next_move)
        pygame.display.update()
    if playagain():
        quitting = False
    else:
        quitting = True


def display_message(window, message, font_size, x, y, font_color):
    img = font_size.render(message, True, font_color)
    display_rect = img.get_rect()
    display_rect.center = (x, y)
    window.blit(img, display_rect)


def playagain():
    pygame.time.delay(2000)
    while True:
        for event in pygame.event.get([pygame.KEYDOWN, pygame.QUIT]):
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                return True
        pygame.time.delay(500)


pygame.init()
GameConfig.init()
Player.init_sprites()
Enemy.init_sprites()
window = pygame.display.set_mode((GameConfig.windowW, GameConfig.windowH))
pygame.display.set_caption("Mortal Battle Mega Fight Kombat Smash Ultimate of Isaac")
pygame.display.set_icon(GameConfig.icon_IMG)
Gameloop(window)
pygame.quit()
quit()
