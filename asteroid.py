from circleshape import CircleShape
import pygame
from constants import *
from logger import *
import random


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        self.line_width = LINE_WIDTH
        self.colour = "White"

        pygame.draw.circle(screen, self.colour, self.position, self.radius, self.line_width)
        return

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self) -> None:
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
    
            log_event("asteroid_split")
            split_direction_pos = random.uniform(20,50)
            split_direction_neg = (split_direction_pos) * (-1)
            new_radii = self.radius - ASTEROID_MIN_RADIUS
            split_asteroid_vector_pos = pygame.Vector2(self.velocity)
            split_asteroid_vector_neg = pygame.Vector2(self.velocity)
            rotated_split_asteroid_vector_pos = split_asteroid_vector_pos.rotate(split_direction_pos)
            rotated_split_asteroid_vector_neg = split_asteroid_vector_pos.rotate(split_direction_neg)
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radii)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radii)
            new_asteroid1.velocity = (pygame.Vector2(rotated_split_asteroid_vector_pos)) * 1.2
            new_asteroid2.velocity = (pygame.Vector2(rotated_split_asteroid_vector_neg)) * 1.2
            


      
