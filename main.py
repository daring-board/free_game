
import pygame
import sys
from player import Player
from enemy import Enemy

def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("アクションゲーム")

    # BGMの読み込みと再生
    pygame.mixer.music.load('assets/sounds/bgm.mp3')
    pygame.mixer.music.play(-1)  # -1でループ再生

    player = Player(400, 500)
    enemy = Enemy(200, 500)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    all_sprites.add(enemy)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        all_sprites.update()

        screen.fill((0, 0, 0))  # 画面を黒で塗りつぶす
        all_sprites.draw(screen)
        pygame.display.flip()  # 画面を更新

        clock.tick(60)  # 60 FPSに設定

if __name__ == "__main__":
    main()
