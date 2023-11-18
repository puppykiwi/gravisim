import math
import pygame
from util import *

class Planet:
    def __init__(self, x, y, mass, display):
        self.x = x
        self.y = y
        self.mass = mass
        self.display = display
    def draw(self):
        self.display.blit(PLANET, (self.x - PLANET_SIZE, self.y - PLANET_SIZE))
