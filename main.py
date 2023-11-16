import math
import pygame

pygame.init()

FPS = 60
WIDTH = 800
HEIGHT = 600

disp = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravitation Slingshot Effect")
pygame.display.set_icon(pygame.image.load("assets/jupiter.png"))

G = 5
SHIP_SIZE = 5
PLANET_SIZE = 50
SHIP_MASS = 5
PLANET_MASS = 100
VEL_SCALE = 100
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

BACKGROUND = pygame.transform.scale(pygame.image.load("assets/background.jpg"), (WIDTH, HEIGHT))
PLANET = pygame.transform.scale(pygame.image.load("assets/jupiter.png"), (PLANET_SIZE * 2, PLANET_SIZE * 2))

class spacecraft:
    def __init__(self, x, y, vel_x, vel_y, mass):
        self.x = int(x)
        self.y = int(y)
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.mass = mass
        
    def move(self, planet=None):
        self.x += self.vel_x
        self.y += self.vel_y
        
    def draw(self):
        pygame.draw.circle(disp, RED, (self.x, self.y), SHIP_SIZE)

def main():
    running = True
    clk = pygame.time.Clock()
    
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
                    t_x, t_y = temp_pos
                    obj = spacecraft(t_x, t_y, 1, 1, SHIP_MASS )
                    objects.append(obj)
                    temp_pos = None
                    
                else:
                    temp_pos = mouse_pos
        
        disp.blit(BACKGROUND, (0, 0))
        
        if temp_pos:
            pygame.draw.line(disp, WHITE, temp_pos, mouse_pos, 2)
            pygame.draw.circle(disp, RED, temp_pos, SHIP_SIZE)
            
        for obj in objects:
            obj.draw()
            obj.move()
            
            
        pygame.display.update()
                
                
                
    pygame.quit()
    
if __name__ == "__main__":
    main()