import pygame

from scripts.entities.enemy import Enemy
import xml.etree.ElementTree as xml

grid = []
grid_size = (0, 0)
current_position = (0, 0)


def Load(filename):
    root = xml.parse(filename).getroot()

    global grid_size
    global current_position

    w, h = int(root.attrib["width"]), int(root.attrib["height"])
    grid_size = (w, h)
    current_position = (int(root.attrib["startX"]), int(root.attrib["startY"]))

    grid.append([])
    i, j = 0, 0
    for level in root:
        enemies = []
        for enemy in level:
            x, y = int(enemy.attrib["x"]), int(enemy.attrib["y"])
            enemies.append((x, y))

        lvl = Level(enemies)
        grid[j].append(lvl)

        i += 1
        if i >= w:
            i = 0
            j += 1
            grid.append([])

        lvl.disable()

    current_level().enable()


def update():
    grid[current_position[0]][current_position[1]].update()


def change_level(dir):
    global current_position
    current_level().disable()
    x = current_position[0] + dir[0]
    x %= grid_size[0]

    if x < 0:
        x += grid_size[0]
    y = current_position[1] + dir[1]
    y %= grid_size[1]
    if y < 0:
        y += grid_size[1]

    current_position = (x, y)
    current_level().enable()


def current_level():
    return grid[current_position[0]][current_position[1]]


def draw(surface):
    current_level().draw(surface)


class Level:
    def __init__(self, enemies=[]):
        self.enemies = pygame.sprite.Group()
        for e in enemies:
            self.enemies.add(Enemy(e))

    def add_enemy(self, pos):
        self.enemies.add(Enemy(pos))

    def update(self):
        for e in self.enemies:
            e.update()

    def draw(self, surface):
        for e in self.enemies:
            e.draw(surface)

    def disable(self):
        for e in self.enemies:
            e.save()
            e.set_position(-40, -40)

    def enable(self):
        for e in self.enemies:
            e.load()

    def is_cleared(self):
        return not (len(self.enemies) > 0)
