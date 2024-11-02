import pygame 
import os

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

AGENT_WIDTH = 100
AGENT_HEIGHT = 120
ENEMY_WIDTH_SMALL = 50
ENEMY_HEIGHT_SMALL = 50
ENEMY_WIDTH_LARGE = 60
ENEMY_HEIGHT_LARGE = 120
ENEMY_HEIGHT_BOSS = 500
ENEMY_WIDTH_BOSS = 250

AGENT_IMG = pygame.transform.scale(pygame.image.load('assets/dai.png'), (AGENT_WIDTH, AGENT_HEIGHT))
ENEMY_SMALL_IMG = pygame.transform.scale(pygame.image.load('assets/turtle.png'), (ENEMY_WIDTH_SMALL, ENEMY_HEIGHT_SMALL))
ENEMY_AIR_IMG = pygame.transform.scale(pygame.image.load('assets/pidgeotto.png'), (ENEMY_WIDTH_SMALL, ENEMY_HEIGHT_SMALL))

ENEMY_LARGE_IMG = [pygame.transform.scale(pygame.image.load(os.path.join("assets/", "creep.png")), (ENEMY_WIDTH_LARGE, ENEMY_HEIGHT_LARGE)),
                   pygame.transform.scale(pygame.image.load(os.path.join("assets/", "king_of_the_night.png")), (ENEMY_WIDTH_LARGE, ENEMY_HEIGHT_LARGE))]

FIRE = pygame.transform.scale(pygame.image.load(os.path.join("assets/", "fire.png")), (40, 40))
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets/", "back_sprite.png")), (SCREEN_WIDTH, SCREEN_HEIGHT))
FONT = pygame.font.Font('freesansbold.ttf', 20)


