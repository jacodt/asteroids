# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH//2
    y = SCREEN_HEIGHT//2
    player = Player(x, y)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    updatable.add(player)
    updatable.add(Asteroid)
    drawable.add(player)
    drawable.add(Asteroid)
    asteroids.add(Asteroid)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
       
        screen.fill(0)
        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
                
        dt = clock.tick(60) / 1000

        for u in updatable:
            u.update(dt)

if __name__ == "__main__":
    main()
