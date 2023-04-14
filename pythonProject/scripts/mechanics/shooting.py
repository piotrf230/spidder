import pygame
from pygame.math import Vector2
from scripts.entities.bullet import Bullet

bullet_pool = pygame.sprite.Group()


def shoot(speed, direction, origin):
    for b in bullet_pool:
        if not b.enabled:
            b.shoot(speed, direction)
            return
    bullet = Bullet()
    bullet.shoot(speed, direction, origin)
    bullet_pool.add(bullet)


def update():
    for b in bullet_pool:
        b.update()