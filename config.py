import pygame

class GameConfig:
    windowH = 640
    windowW = 960
    Y_Platform = 473
    Player_W = 64
    Player_H = 64
    ENEMY_W = 128
    ENEMY_H = 128
    ROCK_W = 10
    ROCK_H = 10
    force_left_player = -20
    force_right_player = -force_left_player
    DT = 0.5
    GRAVITY = 9.81
    FORCEJUMP = -100
    FORCE_ENEMY = 10

    Background_IMG = pygame.image.load('sprites/background.png')
    STANDING_IMG = [pygame.image.load('sprites/walk/stand1.png')]
    JUMP_RIGHT_IMG = [pygame.image.load('sprites/jump.png')]
    JUMP_RIGHT_MASK = [pygame.mask.from_surface(JUMP_RIGHT_IMG[0])]
    JUMP_LEFT_IMG = pygame.transform.flip(pygame.image.load('sprites/jump.png'), True, False)
    ROCK_IMG = pygame.image.load('sprites/rock.png')
    ROCK_IMG_MASK = pygame.image.load('sprites/rock.png')
    ENEMY_LEFT_IMG = pygame.image.load("sprites/enemy_bigger.png")
    ENEMY_RIGHT_IMG = pygame.transform.flip(pygame.image.load("sprites/enemy_bigger.png"), True, False)
    ENEMY_MASK = pygame.mask.from_surface(ENEMY_LEFT_IMG)

    WALK_RIGHT_IMG = [
        pygame.image.load('sprites/walk/walk1.png'),
        pygame.image.load('sprites/walk/walk2.png'),
        pygame.image.load('sprites/walk/walk3.png'),
        pygame.image.load('sprites/walk/walk4.png'),
        pygame.image.load('sprites/walk/walk5.png'),
        pygame.image.load('sprites/walk/walk6.png')
    ]
    WALK_LEFT_IMG = [
       pygame.transform.flip(pygame.image.load('sprites/walk/walk1.png'), True, False),
        pygame.transform.flip(pygame.image.load('sprites/walk/walk2.png'), True, False),
        pygame.transform.flip(pygame.image.load('sprites/walk/walk3.png'), True, False),
        pygame.transform.flip(pygame.image.load('sprites/walk/walk4.png'), True, False),
        pygame.transform.flip(pygame.image.load('sprites/walk/walk5.png'), True, False),
        pygame.transform.flip(pygame.image.load('sprites/walk/walk6.png'), True, False)
    ]

    WALK_RIGHT_MASK = []
    WALK_LEFT_MASK = []
    for im in WALK_RIGHT_IMG:
        WALK_RIGHT_MASK.append(pygame.mask.from_surface(im))
    STANDING_MASK = [pygame.mask.from_surface(STANDING_IMG[0])]
    for im in WALK_LEFT_IMG:
        WALK_LEFT_MASK.append(pygame.mask.from_surface(im))
    NB_FRAMES_PER_SPRITE_PLAYER = 6