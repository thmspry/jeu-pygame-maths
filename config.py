import pygame


class GameConfig:

    # Render font
    def init():
        main_font_path = "assets/fonts/Axis_Extrabold.otf"
        GameConfig.FONT20 = pygame.font.Font(main_font_path, 20)
        GameConfig.FONT150 = pygame.font.Font(main_font_path, 150)

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
    ROCK_W = 30
    ROCK_H = 30
    force_left_player = -30
    force_right_player = -force_left_player
    DT = 0.5
    GRAVITY = 9.81
    RESISTANCE = 0
    FORCEJUMP = -130
    FORCE_ENEMY = 10

    # Images
    icon_IMG = pygame.image.load('assets/images/icon.png')
    Background_IMG = pygame.image.load('assets/images/background_ath.png')
    STANDING_IMG = [pygame.image.load('assets/images/sprites/walk/stand1.png')]
    JUMP_RIGHT_IMG = [pygame.image.load('assets/images/jump.png')]
    JUMP_RIGHT_MASK = [pygame.mask.from_surface(JUMP_RIGHT_IMG[0])]
    JUMP_LEFT_IMG = pygame.transform.flip(pygame.image.load('assets/images/jump.png'), True, False)
    ROCK_IMG = pygame.image.load('assets/images/rock.png')
    ROCK_IMG_MASK = pygame.image.load('assets/images/rock.png')
    ENEMY_LEFT_IMG = pygame.image.load("assets/images/enemy_bigger.png")
    ENEMY_RIGHT_IMG = pygame.transform.flip(pygame.image.load("assets/images/enemy_bigger.png"), True, False)
    ENEMY_MASK = pygame.mask.from_surface(ENEMY_LEFT_IMG)

    # Colors Code (R, G, B)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED_LIFE = (199, 50, 50)  # Rouge pour la barre de vie
    GREY_BAR = (110, 110, 110)  # Gris pour la fond de la barre de vie
    YELLOW_GOLD_WIN = (230, 168, 0)  # Jaune pour le texte "Win"
    RED_DARK_LOSE = (156, 28, 23)  # Rouge pour le texte "Lose"

    # Sprites
    WALK_RIGHT_IMG = [  # Marcher vers la droite
        pygame.image.load('assets/images/sprites/walk/walk1.png'),
        pygame.image.load('assets/images/sprites/walk/walk2.png'),
        pygame.image.load('assets/images/sprites/walk/walk3.png'),
        pygame.image.load('assets/images/sprites/walk/walk4.png'),
        pygame.image.load('assets/images/sprites/walk/walk5.png'),
        pygame.image.load('assets/images/sprites/walk/walk6.png')
    ]
    WALK_LEFT_IMG = [  # Marcher vers la gauche
        pygame.transform.flip(pygame.image.load('assets/images/sprites/walk/walk1.png'), True, False),
        pygame.transform.flip(pygame.image.load('assets/images/sprites/walk/walk2.png'), True, False),
        pygame.transform.flip(pygame.image.load('assets/images/sprites/walk/walk3.png'), True, False),
        pygame.transform.flip(pygame.image.load('assets/images/sprites/walk/walk4.png'), True, False),
        pygame.transform.flip(pygame.image.load('assets/images/sprites/walk/walk5.png'), True, False),
        pygame.transform.flip(pygame.image.load('assets/images/sprites/walk/walk6.png'), True, False)
    ]

    PUNCH_RIGHT_IMG = [  # Coup de poing vers la droite
        pygame.image.load('assets/images/sprites/punch/punch1.png'),
        pygame.image.load('assets/images/sprites/punch/punch2.png'),
        pygame.image.load('assets/images/sprites/punch/punch3.png'),
        pygame.image.load('assets/images/sprites/punch/punch4.png'),
        pygame.image.load('assets/images/sprites/punch/punch5.png')
    ]

    PUNCH_LEFT_IMG = [    # Coup de poing vers la gauche
        pygame.transform.flip(pygame.image.load('assets/images/sprites/punch/punch1.png'), True, False),
        pygame.transform.flip(pygame.image.load('assets/images/sprites/punch/punch2.png'), True, False),
        pygame.transform.flip(pygame.image.load('assets/images/sprites/punch/punch3.png'), True, False),
        pygame.transform.flip(pygame.image.load('assets/images/sprites/punch/punch4.png'), True, False),
        pygame.transform.flip(pygame.image.load('assets/images/sprites/punch/punch5.png'), True, False)
    ]

    PUNCH_FOOT_RIGHT_IMG = [  # Coup de pied vers la droite
        pygame.image.load('assets/images/sprites/punch_foot/punch_foot1.png'),
        pygame.image.load('assets/images/sprites/punch_foot/punch_foot2.png'),
        pygame.image.load('assets/images/sprites/punch_foot/punch_foot3.png'),
        pygame.image.load('assets/images/sprites/punch_foot/punch_foot4.png'),
        pygame.image.load('assets/images/sprites/punch_foot/punch_foot5.png')
    ]

    PUNCH_FOOT_LEFT_IMG = [  # Coup de pied vers la gauche
        pygame.transform.flip(pygame.image.load('assets/images/sprites/punch_foot/punch_foot1.png'), True, False),
        pygame.transform.flip(pygame.image.load('assets/images/sprites/punch_foot/punch_foot2.png'), True, False),
        pygame.transform.flip(pygame.image.load('assets/images/sprites/punch_foot/punch_foot3.png'), True, False),
        pygame.transform.flip(pygame.image.load('assets/images/sprites/punch_foot/punch_foot4.png'), True, False),
        pygame.transform.flip(pygame.image.load('assets/images/sprites/punch_foot/punch_foot5.png'), True, False)
    ]

    # Initilisation des mask de chaque tableau de sprite
    WALK_RIGHT_MASK = []
    WALK_LEFT_MASK = []
    for im in WALK_RIGHT_IMG:
        WALK_RIGHT_MASK.append(pygame.mask.from_surface(im))
    STANDING_MASK = [pygame.mask.from_surface(STANDING_IMG[0])]
    for im in WALK_LEFT_IMG:
        WALK_LEFT_MASK.append(pygame.mask.from_surface(im))

    PUNCH_LEFT_MASK = []
    for im in PUNCH_LEFT_IMG:
        PUNCH_LEFT_MASK.append(pygame.mask.from_surface(im))
    PUNCH_RIGHT_MASK = []
    for im in PUNCH_RIGHT_IMG:
        PUNCH_RIGHT_MASK.append(pygame.mask.from_surface(im))

    PUNCH_FOOT_LEFT_MASK = []
    for im in PUNCH_FOOT_LEFT_IMG:
        PUNCH_FOOT_LEFT_MASK.append(pygame.mask.from_surface(im))
    PUNCH_FOOT_RIGHT_MASK = []
    for im in PUNCH_FOOT_RIGHT_IMG:
        PUNCH_FOOT_RIGHT_MASK.append(pygame.mask.from_surface(im))
    NB_FRAMES_PER_SPRITE_PLAYER = 6
