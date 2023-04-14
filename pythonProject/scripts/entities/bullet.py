import pygame
from pygame.math import Vector2
from scripts.entities.entity import Entity


class Bullet(Entity):
    def __init__(self):
        super().__init__(pygame.image.load("Sprites/bullet.png"), speed=0)
        self.direction = Vector2()
        self.enabled = False

    def shoot(self, speed, direction, origin):
        self.set_position(origin.x, origin.y)
        self.speed = speed
        self.direction = direction
        self.enabled = True

    def update(self) -> None:
        self.move(self.direction)

    def disable(self):
        self.enabled = False
        self.speed = 0
        self.direction = Vector2()
