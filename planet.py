import math
import pygame
from util import *

class Planet:
    def __init__(self, x, y, mass, display, planet):
        self.x = x
        self.y = y
        self.mass = mass
        self.display = display
        self.planet = planet
    def draw(self):
        self.display.blit(self.planet, (self.x - PLANET_SIZE, self.y - PLANET_SIZE))
