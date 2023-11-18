import math
import pygame
from util import *

class Spacecraft:
    def __init__(self, x, y, vel_x, vel_y, mass, display):
        self.x = int(x)
        self.y = int(y)
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.mass = mass
        self.orbit_points = []
        self.disp = display
    
    def move(self, planet=None):
        distance = math.sqrt((self.x - planet.x)**2 + (self.y - planet.y)**2)
        force = (G * self.mass* planet.mass) / distance ** 2
        accel = force / self.mass
        
        theta = math.atan2(planet.y - self.y, planet.x - self.x)
        
        accel_x = accel * math.cos(theta)
        accel_y = accel * math.sin(theta)
        
        self.vel_x += accel_x
        self.vel_y += accel_y
        
        self.x += self.vel_x
        self.y += self.vel_y
        
        self.orbit_points.append((self.x, self.y))

        if len(self.orbit_points) > 150:
            self.orbit_points.pop(0)

    def draw(self):
        for point in self.orbit_points:
            pygame.draw.circle(self.disp, GREY, (int(point[0]), int(point[1])), 1)
        pygame.draw.circle(self.disp, RED, (self.x, self.y), SHIP_SIZE)