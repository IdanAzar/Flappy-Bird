import pygame

# Init Font
pygame.font.init()

# set window size
SCREEN_WIDTH = 500

SCREEN_HEIGHT = 800

SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Array of bird images to animate on screen
BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load("Assets/redbird-upflap.png")),
             pygame.transform.scale2x(pygame.image.load("Assets/redbird-midflap.png")),
             pygame.transform.scale2x(pygame.image.load("Assets/redbird-downflap.png"))]

# Load pipe image
PIPE_IMG = pygame.transform.scale2x(pygame.image.load("Assets/pipe-green.png"))

# Load Base floor image
BASE_IMG = pygame.transform.scale2x(pygame.image.load("Assets/base.png"))

# Load background image
BG_IMG = pygame.transform.scale2x(pygame.image.load("Assets/background-day.png"))

# bird jumping velocity
VEL_JUMP = -10.5

# set bird gravity
GRAVITY = 3

# set max distance that the bird can do while jumping
MAX_DISTANCE = 16

# set min distance that the bird can do while jumping
MIN_DISTANCE = 2

# starting position of bird
BIRD_START_POS = (230, 350)

# starting position of base
BASE_START_POS = 730

# starting position of pipe
PIPE_START_POS = 700

# pipe mid-game position of pipe
PIPE_MID_POS = 600

# font for display score
STATS_FONT = pygame.font.SysFont("comicsansms", 40)

# set generation size
GEN_SIZE = 30
