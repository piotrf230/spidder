import pygame.sprite

health_bar = []


def init_health(health):
    for i in range(health):
        health_bar.append(Heart((20, 600 - (20 + i * 36))))


def take_hit() -> bool:
    health_bar.pop(len(health_bar) - 1)
    return len(health_bar) <= 0

def draw(surface):
    for h in health_bar:
        h.draw(surface)


class Heart(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load("Sprites/heart.png")
        self.rect = self.image.get_rect()
        self.rect.center = position

    def draw(self, surface):
        surface.blit(self.image, self.rect)
