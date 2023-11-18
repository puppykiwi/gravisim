import math
import pygame

FPS = 120
WIDTH = 800
HEIGHT = 600

G = 5
SHIP_SIZE = 5
PLANET_SIZE = 50
SHIP_MASS = 5
PLANET_MASS = 100
VEL_SCALE = 100
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (122, 122, 122)
WHITE = (255, 255, 255)

BACKGROUND = pygame.transform.scale(pygame.image.load("assets/background.jpg"), (WIDTH, HEIGHT))
PLANET = pygame.transform.scale(pygame.image.load("assets/jupiter.png"), (PLANET_SIZE * 2, PLANET_SIZE * 2))