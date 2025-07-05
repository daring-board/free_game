
import pygame
import sys
from player import Player
from enemy import Enemy

def main():
    pygame.init()
    pygame.mixer.init()
    screen_width = 800
    screen = pygame.display.set_mode((screen_width, 600))
    pygame.display.set_caption("アクションゲーム")

    # BGMの読み込みと再生
    pygame.mixer.music.load('assets/sounds/bgm.mp3')
    pygame.mixer.music.play(-1)  # -1でループ再生

    player = Player(400, 500)
    enemies = pygame.sprite.Group()
    enemy = Enemy(200, 500, screen_width)
    enemies.add(enemy)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    all_sprites.add(enemies)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        all_sprites.update()

        # プレイヤーと敵の衝突判定
        collided_enemies = pygame.sprite.spritecollide(player, enemies, False)
        for enemy in collided_enemies:
            # プレイヤーが落下中 (vel_y > 0) で、プレイヤーの足が敵の頭の上にある場合に敵を倒す
            if player.vel_y > 0 and player.rect.bottom < enemy.rect.centery:
                enemy.kill()

        screen.fill((0, 0, 0))  # 画面を黒で塗りつぶす
        all_sprites.draw(screen)
        pygame.display.flip()  # 画面を更新

        clock.tick(60)  # 60 FPSに設定

if __name__ == "__main__":
    main()
