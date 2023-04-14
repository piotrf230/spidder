import sys
import time

import pygame
from pygame.locals import *

from scripts.entities.player import Player
from scripts.entities.enemy import Enemy


def entity_collide(entity, collide_group) -> bool:
    return pygame.sprite.spritecollideany(entity, collide_group)


windowSize = (600, 600)

pygame.init()

FPS = 60
FPSClock = pygame.time.Clock()

displaySurface = pygame.display.set_mode(windowSize)

player = Player()
player.set_position(150, 150)

enemies = pygame.sprite.Group()
enemies.add(Enemy((500, 500)))
enemies.add(Enemy((400, 500)))
enemies.add(Enemy((500, 400)))
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
for e in enemies:
    all_sprites.add(e)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # logic

    for s in all_sprites:
        s.update()

    if entity_collide(player, enemies):
        displaySurface.fill((255, 0, 0))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # draw
    displaySurface.fill((255, 255, 255))
    for s in all_sprites:
        s.draw(displaySurface)
    pygame.display.update()
    FPSClock.tick(FPS)
