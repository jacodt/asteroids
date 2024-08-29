import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.position = pygame.Vector2(x,y)
        self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(screen,(255,0,0), (int(self.position.x), int(self.position.y)), self.radius, 2)
        