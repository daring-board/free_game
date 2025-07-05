
import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, screen_width):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255))  # 青色の四角形
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 2
        self.screen_width = screen_width

    def update(self):
        self.rect.x += self.speed
        if self.rect.left < 0 or self.rect.right > self.screen_width:
            self.speed = -self.speed
