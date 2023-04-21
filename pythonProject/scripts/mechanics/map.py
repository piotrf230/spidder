import pygame
import scripts.mechanics.levels as levels


class MapPoint(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.states = \
            {'default': pygame.image.load("Sprites/dot.png"),
             'current': pygame.image.load("Sprites/dotfull.png"),
             'default_cleared': pygame.image.load("Sprites/dotcleared.png"),
             'current_cleared': pygame.image.load("Sprites/dotfullcleared.png")}
        self.image = self.states['default']
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.cleared = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def switch(self, current):
        self.image = self.states[("current" if current else "default") + ("_cleared" if self.cleared else "")]


class MiniMap:
    def __init__(self):
        self.current = (-1, -1)
        self.map = []
        x = 12
        for j in range(levels.grid_size[1]):
            self.map.append([])
            y = 12
            for i in range(levels.grid_size[0]):
                self.map[j].append(MapPoint((x, y)))
                y += 20
            x += 20
        self.update()

    def update(self):
        for j in range(levels.grid_size[1]):
            for i in range(levels.grid_size[0]):
                self.map[j][i].cleared = levels.grid[j][i].is_cleared()

        if self.current != levels.current_position:
            self.map[self.current[0]][self.current[1]].switch(False)
            self.map[levels.current_position[0]][levels.current_position[1]].switch(True)
            self.current = levels.current_position

    def draw(self, surface):
        for a in self.map:
            for mp in a:
                mp.draw(surface)
