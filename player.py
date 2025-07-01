
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # 赤色の四角形
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.vel_y = 0
        self.on_ground = False
        self.jump_sound = pygame.mixer.Sound('assets/sounds/jump.mp3')

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # 重力
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        self.rect.y += self.vel_y

        # 地面との当たり判定
        if self.rect.bottom > 600:
            self.rect.bottom = 600
            self.vel_y = 0
            self.on_ground = True
        else:
            self.on_ground = False

        # ジャンプ
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = -20
            self.on_ground = False
            self.jump_sound.play()
