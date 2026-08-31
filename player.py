from constants import *
from circleshape import CircleShape
import pygame


class Player(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.radius = PLAYER_RADIUS
        self.y = y
        self.x = x
        self.rotation = 0
        return

    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface):
        self.line_width = LINE_WIDTH
        self.colour = "White"
        self.points = self.triangle()

        pygame.draw.polygon(screen, self.colour, self.points, self.line_width)
        return
