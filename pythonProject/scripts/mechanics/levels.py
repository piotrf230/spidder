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
            grid[j].append(Level(['N', 'E', 'S', 'W']))
    gridSize = (width, height)


class Level():
    def __init__(self, openDoors=[], enemyPositions=[]):
        self.enemies = []
        self.doorways = {'N': 'N' in openDoors, 'E': 'E' in openDoors, 'S': 'S' in openDoors, 'W': 'W' in openDoors}
        for pos in enemyPositions:
            self.add_enemy(pos[0], pos[1])

    def add_enemy(self, x, y):
        self.enemies.add(Enemy(x, y))
