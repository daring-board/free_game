
import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255))  # 青色の四角形
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
