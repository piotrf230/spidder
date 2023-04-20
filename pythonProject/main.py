import sys
import time

import pygame
from pygame.locals import *

import scripts.mechanics.shooting as shooting
import scripts.mechanics.levels as levels

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
player.set_position(300, 550)

levels.Load("Levels/Levels.xml")
move = None

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # logic
    player.update()
    shooting.update()

    for e in levels.current_level().enemies:
        e.set_target(player.get_position())

    if entity_collide(player, levels.current_level().enemies):
        displaySurface.fill((255, 0, 0))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    p = player.get_position()
    d = pygame.display.get_window_size()

    if p[0] < 0:
        player.set_position(p[0] + d[0], p[1])
        levels.change_level((-1, 0))
    elif p[0] > d[0]:
        player.set_position(p[0] - d[0], p[1])
        levels.change_level((1, 0))
    elif p[1] < 0:
        player.set_position(p[0], p[1] + d[1])
        levels.change_level((0, -1))
    elif p[1] > d[1]:
        player.set_position(p[0], p[1] - d[1])
        levels.change_level((0, 1))

    levels.update()

    # draw
    displaySurface.fill((56, 156, 56))
    shooting.draw_bullets(displaySurface)
    player.draw(displaySurface)
    levels.draw(displaySurface)

    pygame.display.update()
    FPSClock.tick(FPS)
