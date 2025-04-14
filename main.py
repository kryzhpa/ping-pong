import pygame
import sys
import time

# Инициализация игры
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ping Pong')

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (52, 235, 229)
GREEN = (52, 235, 89)
PINK = (227, 34, 224)
PURPLE =(178, 17, 237)

# Настройки ракеток и мяча
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 15
ball_speed = [5, 5]

# Позиции и скорости
player1 = pygame.Rect(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2 = pygame.Rect(WIDTH - 40, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)

clock = pygame.time.Clock()

# Скорость игроков
speed_player1 = 0
speed_player2 = 0

# Счетчики
score_player1 = 0
score_player2 = 0
start_time = time.time()

# Шрифт
font = pygame.font.SysFont('Arial', 36)

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                speed_player1 = -5
            elif event.key == pygame.K_s:
                speed_player1 = 5
            elif event.key == pygame.K_UP:
                speed_player2 = -5
            elif event.key == pygame.K_DOWN:
                speed_player2 = 5
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_s):
                speed_player1 = 0
            elif event.key in (pygame.K_UP, pygame.K_DOWN):
                speed_player2 = 0

    # Движение ракеток
    player1.y += speed_player1
    player2.y += speed_player2

    # Ограничение ракеток
    player1.y = max(0, min(player1.y, HEIGHT - PADDLE_HEIGHT))
    player2.y = max(0, min(player2.y, HEIGHT - PADDLE_HEIGHT))

    # Движение мяча
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Проверка столкновений
    if ball.y <= 0 or ball.y >= HEIGHT - BALL_SIZE:
        ball_speed[1] = -ball_speed[1]

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed[0] = -ball_speed[0]

    # Рестарт мяча и обновление счета
    if ball.x <= 0:
        score_player2 += 1
        ball.x, ball.y = WIDTH // 2, HEIGHT // 2
        ball_speed[0] = -ball_speed[0]
    elif ball.x >= WIDTH:
        score_player1 += 1
        ball.x, ball.y = WIDTH // 2, HEIGHT // 2
        ball_speed[0] = -ball_speed[0]

    # Отрисовка
    screen.fill(PINK)
    pygame.draw.rect(screen, BLUE, player1)
    pygame.draw.rect(screen, BLUE, player2)
    pygame.draw.ellipse(screen, BLACK, ball)
    pygame.draw.aaline(screen, BLACK, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Отображение счета
    score_text = font.render(f'{score_player1} : {score_player2}', True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

    # Отображение таймера
    elapsed_time = int(time.time() - start_time)
    timer_text = font.render(f'Time: {elapsed_time} sec', True, WHITE)
    screen.blit(timer_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)


