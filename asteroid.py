
import pygame
import random

from circleshape import CircleShape
from logger import log_state, log_event
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius,
                LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        rand_degrees = random.uniform(20, 50)

        new_vel_1 = self.velocity.rotate(rand_degrees)
        new_vel_2 = self.velocity.rotate(-rand_degrees)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        x = self.position.x
        y = self.position.y

        asteroid1 = Asteroid(x, y, new_radius)
        asteroid2 = Asteroid(x, y, new_radius)

        asteroid1.velocity = new_vel_1
        asteroid2.velocity = new_vel_2
