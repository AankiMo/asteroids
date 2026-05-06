import pygame, random
from constants import *
from circleshape import CircleShape
from logger import log_event

class Asteroids(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, ASTEROID_COLOR, self.position, self.radius, LINE_WIDTH)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        split_angle = random.uniform(20,50)
        new_dir_1 = self.velocity.rotate(split_angle)
        new_dir_2 = self.velocity.rotate(-split_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_ast_1 = Asteroids(self.position.x, self.position.y, new_radius)
        new_ast_2 = Asteroids(self.position.x, self.position.y, new_radius)
        new_ast_1.velocity = new_dir_1
        new_ast_2.velocity = new_dir_2
    
    def update(self, dt):
        self.position += self.velocity * dt