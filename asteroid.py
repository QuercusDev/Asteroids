from circleshape import CircleShape
import pygame
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        self.line_width = LINE_WIDTH
        self.colour = "White"

        self.radius = ASTEROID_MIN_RADIUS
        self.position = pygame.Vector2(2,2)

        pygame.draw.circle(screen, self.colour, self.position, self.radius, self.line_width)
        return

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    