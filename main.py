import pygame
from constants import *

def main():
    # Screen dimension
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop
    while True:
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Render Screen
        screen.fill((0,0,0))
        # Refresh the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()
