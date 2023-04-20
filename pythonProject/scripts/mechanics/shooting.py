import pygame
from scripts.entities.bullet import Bullet

bullet_pool = pygame.sprite.Group()


def shoot(speed, direction, origin):
    for b in bullet_pool:
        if not b.enabled:
            b.shoot(speed, direction, origin)
            return
    bullet = Bullet()
    bullet.shoot(speed, direction, origin)
    bullet_pool.add(bullet)


def update():
    for b in bullet_pool:
        b.update()

def clear_screen():
    for b in bullet_pool:
        b.disable()

def draw_bullets(surface):
    for b in bullet_pool:
        if b.enabled:
            b.draw(surface)
