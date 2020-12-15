import pygame

class GameConfig:
    windowH = 640
    windowW = 960
    Y_Platform = 516
    Player_W = 64
    Player_H = 64
    force_left_player = -20
    force_right_player = -force_left_player
    DT = 0.5
    Background_IMG = pygame.image.load('sprites/background.png')
    STANDING_IMG = [pygame.image.load('sprites/walk/stand1.png')]
    WALK_RIGHT_IMG = [
        pygame.image.load('sprites/walk/walk1.png'),
        pygame.image.load('sprites/walk/walk2.png'),
        pygame.image.load('sprites/walk/walk3.png'),
        pygame.image.load('sprites/walk/walk4.png'),
        pygame.image.load('sprites/walk/walk5.png'),
        pygame.image.load('sprites/walk/walk6.png')
    ]
    WALK_RIGHT_MASK = []
    for im in WALK_RIGHT_IMG:
        WALK_RIGHT_MASK.append(pygame.mask.from_surface(im))
    STANDING_MASK = [pygame.mask.from_surface(STANDING_IMG[0])]
    NB_FRAMES_PER_SPRITE_PLAYER = 6