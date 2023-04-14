import pygame
from pygame.math import Vector2
from scripts.entities.entity import Entity
import scripts.mechanics.shooting as shooting


class Player(Entity):

    def __init__(self):
        super().__init__(pygame.image.load("Sprites/player.png"), (150, 150))
        self.shoot_direction = Vector2(1, 0)

    def update(self):
        pressed = pygame.key.get_pressed()
        mv = Vector2()

        if pressed[pygame.K_UP]:
            mv.y -= 1
        if pressed[pygame.K_DOWN]:
            mv.y += 1
        if pressed[pygame.K_LEFT]:
            mv.x -= 1
        if pressed[pygame.K_RIGHT]:
            mv.x += 1

        if mv.length() > 0.001:
            self.shoot_direction = mv

        if pressed[pygame.K_SPACE]:
            center = self.rect.center
            shooting.shoot(8, self.shoot_direction, Vector2(center[0], center[1]))

        self.move(mv)
