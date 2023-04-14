import pygame.sprite


class Entity(pygame.sprite.Sprite):
    def __init__(self, sprite, position=(0, 0), speed=5):
        super().__init__()
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.speed = speed

    def move(self, direction):
        if direction.length() == 0:
            return
        direction.normalize_ip()
        direction *= self.speed
        self.rect.move_ip(direction)

    def set_position(self, x, y):
        self.rect.center = (x, y)

    def get_position(self):
        return self.rect.center

    def draw(self, surface):
        surface.blit(self.image, self.rect)
