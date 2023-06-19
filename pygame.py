import pygame
import sys

# 초기화
pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("간단한 FPS 게임")

# 플레이어 설정
player_x = screen_width // 2
player_y = screen_height // 2
player_radius = 10
player_color = (255, 0, 0)

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 플레이어 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5
    if keys[pygame.K_UP]:
        player_y -= 5
    if keys[pygame.K_DOWN]:
        player_y += 5

    # 화면 업데이트
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, player_color, (player_x, player_y), player_radius)
    pygame.display.flip()
