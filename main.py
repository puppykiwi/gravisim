import math
from util import *
import pygame
from planet import Planet


pygame.init()
global disp
disp = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravitation Slingshot Effect")
pygame.display.set_icon(pygame.image.load("assets/jupiter.png"))

class spacecraft:
    def __init__(self, x, y, vel_x, vel_y, mass):
        self.x = int(x)
        self.y = int(y)
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.mass = mass
        self.orbit_points = []
    
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
            pygame.draw.circle(disp, GREY, (int(point[0]), int(point[1])), 1)
        pygame.draw.circle(disp, RED, (self.x, self.y), SHIP_SIZE)

# class Planet:
#     def __init__(self, x, y, mass):
#         self.x = x
#         self.y = y
#         self.mass = mass
    
#     def draw(self):
#         disp.blit(PLANET, (self.x - PLANET_SIZE, self.y - PLANET_SIZE))
        
        

def create_ship(Location, mouse):
    t_x, t_y = Location
    m_x, m_y = mouse
    vel_x = (m_x - t_x) / VEL_SCALE
    vel_y = (m_y - t_y) / VEL_SCALE
    obj = spacecraft(t_x, t_y, vel_x, vel_y, SHIP_MASS) #class call
    return obj

def control(key):
    global VEL_SCALE
    if (key == pygame.K_UP) & (VEL_SCALE > 10):
        VEL_SCALE -= 10
        print("Velocity: ", int((10 - (VEL_SCALE / 10))))
        
    elif (key == pygame.K_DOWN) & (VEL_SCALE < 100):
        VEL_SCALE += 10
        print("Velocity: ", int((10 - (VEL_SCALE / 10))))
        
    global G
    if (key == pygame.K_RIGHT) & (G < 11):
        G += 1
        print("Gravity: ", G)
        
    elif (key == pygame.K_LEFT) & (G > 1):
        G -= 1
        print("Gravity: ", G)

def main():
    running = True
    clk = pygame.time.Clock()
    
    planet = Planet(WIDTH // 2, HEIGHT // 2, PLANET_MASS, disp, PLANET)
    objects = []
    temp_pos = None
    
    while running:
        clk.tick(FPS)
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if temp_pos:
                    obj = create_ship(temp_pos, mouse_pos)
                    objects.append(obj)
                    temp_pos = None
                    
                else:
                    temp_pos = mouse_pos
                    
            if event.type == pygame.KEYDOWN:
                control(event.key)
        
        disp.blit(BACKGROUND, (0, 0))
        
        if temp_pos:
            pygame.draw.line(disp, WHITE, temp_pos, mouse_pos, 2)
            pygame.draw.circle(disp, RED, temp_pos, SHIP_SIZE)
            
        for obj in objects:
            obj.draw()
            obj.move(planet)
            off_screen = obj.x < 0 or obj.x > WIDTH or obj.y < 0 or obj.y > HEIGHT
            collided = math.sqrt((obj.x - planet.x)**2 + (obj.y - planet.y)**2) <= PLANET_SIZE
            if off_screen or collided:
                objects.remove(obj)
                
        
        planet.draw()
        pygame.display.update()
                  
    pygame.quit()
    
if __name__ == "__main__":
    main()