import sys

import pygame
from config import *
from Player import *
from GameState import *
from Move import *


# Fonction pour récupérer le mouvement voulu du joueur suivant la touche appuyée.
def get_next_move():
    next_move = Move()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        next_move.right = True
    if keys[pygame.K_LEFT]:
        next_move.left = True
    if keys[pygame.K_UP]:
        next_move.up = True
    if keys[pygame.K_x]:
        next_move.punch = True
    if keys[pygame.K_c]:
        next_move.punch_foot = True
    if keys[pygame.K_w]:
        next_move.tir = True
    return next_move


# Boucle de jeu
def game_loop(window):
    game_state = GameState()
    quitting = False  # Indicateur de fin de jeu
    while not quitting:
        pygame.time.delay(20)
        game_state.draw(window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if game_state.is_win():
            display_message(window, "You WIN", GameConfig.FONT150, GameConfig.windowW / 2, GameConfig.windowH / 2 - 50,
                            GameConfig.YELLOW_GOLD_WIN)
            display_message(window, "Press R to restart, or close the window to quit", GameConfig.FONT20, GameConfig.windowW / 2,
                            GameConfig.windowH / 2 + 50, GameConfig.BLACK)
            quitting = True

        if game_state.is_lose():
            display_message(window, "You LOSE", GameConfig.FONT150, GameConfig.windowW / 2, GameConfig.windowH / 2 - 50,
                            GameConfig.RED_DARK_LOSE)
            display_message(window, "Press R to restart, or close the window to quit", GameConfig.FONT20, GameConfig.windowW / 2,
                            GameConfig.windowH / 2 + 50, GameConfig.BLACK)
            quitting = True
        # LIGNES A COMMENTER/DECOMMENTER (UNE A LA FOIS)
        next_move = get_next_move()  # DÉCOMMENTER SI ON VEUT JOUER PAR SOIT MÊME
        # next_move = game_state.get_ia_command()  # DÉCOMMENTER SI ON VEUT JOUER AVEC L'IA
        game_state.advance_state(next_move)
        pygame.display.update()
    if play_again():
        game_loop(window)


# Afficher un message avec la font disponible dans assets/fonts
def display_message(window, message, font_size, x, y, font_color):
    img = font_size.render(message, True, font_color)
    display_rect = img.get_rect()
    display_rect.center = (x, y)
    window.blit(img, display_rect)


# Determine si le joueur veux jouer a nouveau
def play_again():
    pygame.time.delay(2000)  # On attends 2 secondes
    while True:
        for event in pygame.event.get([pygame.K_r, pygame.QUIT]):
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.K_r:
                return True
        pygame.time.delay(5)


pygame.init()
GameConfig.init()
Player.init_sprites()
Enemy.init_sprites()
window = pygame.display.set_mode((GameConfig.windowW, GameConfig.windowH))
pygame.display.set_caption("Mortal Battle Mega Fight Kombat Smash Ultimate of Isaac")
pygame.display.set_icon(GameConfig.icon_IMG)
game_loop(window)
pygame.quit()
quit()
