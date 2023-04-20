import pygame

from scripts.entities.enemy import Enemy

grid = []
grid_size = (0, 0)
current_position = (0, 0)


def Generate(width, height):
    global grid_size
    grid_size = (width, height)
    for j in range(height):
        grid.append([])
        for i in range(width):
            grid[j].append(Level([(200, 300), (400, 300)]))
            grid[j][i].disable()


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
