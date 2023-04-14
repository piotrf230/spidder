import pygame
from pygame.math import Vector2
from Scripts.Entity import Entity


class Enemy(Entity):
    def __init__(self, position, target=None):
        super().__init__(pygame.image.load("Sprites/enemy.png"), position=position, speed=3)
        self.target = target

    def set_target(self, target_position) -> None:
        self.target = target_position

    def update(self):
        if self.target == None:
            return
        t, c = self.target, self.rect.center
        mv = Vector2(t[0] - c[0], t[1] - c[1])
        self.move(mv)
