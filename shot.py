import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius=SHOT_RADIUS):
        super().__init__(x,y,radius)
        self.position = pygame.Vector2(x,y)
        self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", 
                           (int(self.position.x), 
                            int(self.position.y)), 
                            self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

        
        