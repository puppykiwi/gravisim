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
OBJ_SIZE = 5
PLANET_SIZE = 50
SHIP_MASS = 5
PLANET_MASS = 100
VEL_SCALE = 100
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

BACKGROUND = pygame.transform.scale(pygame.image.load("assets/background.jpg"), (WIDTH, HEIGHT))
PLANET = pygame.transform.scale(pygame.image.load("assets/jupiter.png"), (PLANET_SIZE * 2, PLANET_SIZE * 2))

def main():
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
                
                
    pygame.quit()
    
if __name__ == "__main__":
    main()