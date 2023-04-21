import sys
import time

import pygame
from pygame.locals import *

import scripts.mechanics.shooting as shooting
import scripts.mechanics.levels as levels
import scripts.mechanics.health as health
from scripts.mechanics.map import MiniMap

from scripts.entities.player import Player

colors = {
    "black": (0, 0, 0),
    "red": (255, 51, 0),
    "green": (64, 156, 32),
    "white": (255, 255, 255),
    "grass": (0, 153, 51)
}


def show_text(message, surface, pos, color):
    text = font.render(message, True, color)
    rect = text.get_rect()
    center = (pos[0] - rect.w / 2, pos[1] - rect.h / 2)
    surface.blit(text, center)


windowSize = (600, 600)

pygame.init()

pygame.display.set_caption("Spidder")
font = pygame.font.SysFont(None, 72, True)

FPS = 60
FPSClock = pygame.time.Clock()

displaySurface = pygame.display.set_mode(windowSize)

player = Player()
player.set_position(300, 300)
health.init_health(3)

levels.Load("Levels/Levels.xml")
mm = MiniMap()

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

    hit = pygame.sprite.spritecollideany(player, levels.current_level().enemies)
    if hit:
        hit.kill()
        if health.take_hit():
            displaySurface.fill(colors["red"])
            show_text("You Lost!", displaySurface, (windowSize[0] / 2, windowSize[1] / 2), colors["white"])
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            sys.exit()
    elif levels.check_win():
        displaySurface.fill(colors["green"])
        show_text("You Won!", displaySurface, (windowSize[0] / 2, windowSize[1] / 2), colors["white"])
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    p = player.get_position()
    d = pygame.display.get_window_size()

    if p[0] < 0:
        player.set_position(p[0] + d[0], p[1])
        levels.change_level((-1, 0))
        shooting.clear_screen()
    elif p[0] > d[0]:
        player.set_position(p[0] - d[0], p[1])
        levels.change_level((1, 0))
        shooting.clear_screen()
    elif p[1] < 0:
        player.set_position(p[0], p[1] + d[1])
        levels.change_level((0, -1))
        shooting.clear_screen()
    elif p[1] > d[1]:
        player.set_position(p[0], p[1] - d[1])
        levels.change_level((0, 1))
        shooting.clear_screen()

    levels.update()
    mm.update()

    # draw
    displaySurface.fill(colors["grass"])
    shooting.draw_bullets(displaySurface)
    player.draw(displaySurface)
    levels.draw(displaySurface)
    mm.draw(displaySurface)
    health.draw(displaySurface)

    pygame.display.update()
    FPSClock.tick(FPS)
