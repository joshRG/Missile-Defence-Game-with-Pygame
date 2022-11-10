import pygame
SCREENSIZE = [960, 540]

#General Settings
FPS = 30
TITLE = "Atari Missile Command"
SHOW_MOUSE = True
current_game_state = 0
GAME_STATE_SPLASH = 10
GAME_STATE_RUNNING = 20
GAME_STATE_MENU = 30
GAME_STATE_NEW_LEVEL = 40
GAME_STATE_OVER = 50
NUM_CITIES = 8
SKY_LEVEL = 35
GROUND_LEVEL = 20
INTERCEPT_RADIUS = 35
NUKE_RADIUS = 50

#Colors

BACKGROUND = (0, 0, 0)
GROUND = (69, 139, 81)
DEFENCE = (48, 117, 213)
CITY = (255, 211, 24)
WARHEAD = (255, 0, 0)
WARHEAD_TRAIL = (204, 39, 36)
INTERCEPTER = (48, 117, 213)
INTERCEPTER_TRAIL = (255, 255, 255)
INTERCEFACE_PRI = (69, 139, 116)
INTERFACE_SEC = (69, 127, 139)
NUKE_EXPLOSION = (255, 0, 0)
INTERCEPTER_EXPLOSION = (255, 255, 255)

#Game Font

pygame.font.init()
file_font = "data\snt\PressStart2P-Regular.ttf"
game_font = pygame.font.Font(file_font, 16)