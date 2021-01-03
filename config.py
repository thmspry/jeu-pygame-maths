import pygame


class GameConfig:

    # Render font
    def init():
        GameConfig.FONT20 = pygame.font.Font('sprites/Axis_Extrabold.otf', 20)
        GameConfig.FONT150 = pygame.font.Font('sprites/Axis_Extrabold.otf', 150)

    # Useful values
    windowH = 720
    windowW = 1080
    Y_GROUND = 600
    Y_PLATFORMS = [550, 400]
    X_PLATFORMS = [100, 300]
    PLATFORM_W = 100
    Player_W = 64
    Player_H = 64
    ENEMY_W = 128
    ENEMY_H = 128
    ROCK_W = 10
    ROCK_H = 10
    force_left_player = -30
    force_right_player = -force_left_player
    DT = 0.5
    GRAVITY = 9.81
    FORCEJUMP = -100
    FORCE_ENEMY = 10

    # Images
    Background_IMG = pygame.image.load('sprites/background_ath.png')
    STANDING_IMG = [pygame.image.load('sprites/walk/stand1.png')]
    JUMP_RIGHT_IMG = [pygame.image.load('sprites/jump.png')]
    JUMP_RIGHT_MASK = [pygame.mask.from_surface(JUMP_RIGHT_IMG[0])]
    JUMP_LEFT_IMG = pygame.transform.flip(pygame.image.load('sprites/jump.png'), True, False)
    ROCK_IMG = pygame.image.load('sprites/rock.png')
    ROCK_IMG_MASK = pygame.image.load('sprites/rock.png')
    ENEMY_LEFT_IMG = pygame.image.load("sprites/enemy_bigger.png")
    ENEMY_RIGHT_IMG = pygame.transform.flip(pygame.image.load("sprites/enemy_bigger.png"), True, False)
    ENEMY_MASK = pygame.mask.from_surface(ENEMY_LEFT_IMG)

    # Colors Code (R, G, B)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED_LIFE = (199, 50, 50)
    GREY_BAR = (110, 110, 110)
    YELLOW_GOLD_WIN = (230, 168, 0)
    RED_DARK_LOSE = (156, 28, 23)

    # Sprites
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
