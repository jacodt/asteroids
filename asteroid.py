import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
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

        
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        new_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(new_angle)
        new_velocity2 = self.velocity.rotate(-new_angle)
        new_asteroid1 = Asteroid(self.position.x,self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        new_asteroid1.velocity = new_velocity1*1.2
        new_asteroid2 = Asteroid(self.position.x,self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        new_asteroid2.velocity = new_velocity2*1.2


        