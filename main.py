import pygame
from constants import *
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    clock = pygame.time.Clock()
    dt = 0.0
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    starting_x = SCREEN_WIDTH / 2
    starting_y = SCREEN_HEIGHT / 2
    player1 = Player(starting_x, starting_y)
    asteroidfield = AsteroidField()
    while True:
        log_state()
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
                return
        screen.fill("black")
        dt = clock.tick(60)/1000
        updatable.update(dt)
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()   
        

if __name__ == "__main__":
    main()
