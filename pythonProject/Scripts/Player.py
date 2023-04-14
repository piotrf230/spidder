import pygame
from pygame.math import Vector2
from Scripts.Entity import Entity


class Player(Entity):

    def __init__(self):
        super().__init__(pygame.image.load("Sprites/player.png"), (150, 150))

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

        self.move(mv)