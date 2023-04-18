from scripts.entities.enemy import Enemy

grid = []
grid_size = (0, 0)
current_position = (0, 0)


def Generate(width, height):
    __GenerateGrid(width, height)


def __GenerateGrid(width, height):
    for j in range(height):
        grid.append([])
        for i in range(width):
            grid[j].append(Level())
    gridSize = (width, height)


class Level:
    def __init__(self, enemies=[]):
        self.enemies = enemies

    def add_enemy(self, x, y):
        self.enemies.add(Enemy(x, y))
