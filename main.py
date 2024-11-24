import sys
import pygame
from constants import *
from player import *
from asteroids import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    # Screen dimension
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Group 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Player init
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Asterodis init
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    # Shots init
    Shot.containers = (shots, updatable, drawable)

    dt = 0

    # Game loop
    while True:
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Render Screen
        screen.fill((0,0,0))
        # Update the movements
        for obj in updatable:
            obj.update(dt)
        # Draw the player
        for obj in drawable:
            obj.draw(screen)
        # Check player collision
        for obj in asteroids:
            if obj.collide(player):
                # print("Game over!")
                sys.exit("Game over!")
        # Check bullet collision
        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.collide(bullet):
                    asteroid.split()
        # Refresh the screen
        pygame.display.flip()
        dt = clock.tick(60)
        dt /= 1000

if __name__ == "__main__":
    main()
