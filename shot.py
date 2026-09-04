from circleshape import CircleShape
from constants import *
import pygame




class Shot(CircleShape):
    def __init__ (self, x: float, y: float):
        super().__init__(x, y, SHOT_RADIUS)
        self.x = x
        self.y = y
        self.radius = SHOT_RADIUS

    def draw(self, screen: pygame.Surface):
        self.line_width = LINE_WIDTH
        self.colour = "White"
        pygame.draw.circle(screen, self.colour, self.position, self.radius, self.line_width)
        return
        
    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)
        