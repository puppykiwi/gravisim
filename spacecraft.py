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

