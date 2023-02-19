import pygame
import random
from pygame.locals import *
import constant


def on_grid_random():
    x = random.randint(0, 620)
    y = random.randint(0, 460)
    return (x//10 * 10, y//10 * 10)


def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


pygame.init()
screen = pygame.display.set_mode((constant.GAME_WIDTH, constant.GAME_HEIGHT))
pygame.display.set_caption(constant.GAME_TITLE)
font = pygame.font.Font(None, 50)

snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((0, 200, 0))

apple_pos = on_grid_random()
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))

my_direction = K_LEFT

clock = pygame.time.Clock()

while True:
    clock.tick(constant.GAME_FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP or event.key == ord('w'):
                my_direction = K_UP
            if event.key == K_DOWN or event.key == ord('s'):
                my_direction = K_DOWN
            if event.key == K_RIGHT or event.key == ord('d'):
                my_direction = K_RIGHT
            if event.key == K_LEFT or event.key == ord('a'):
                my_direction = K_LEFT

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0, 0))

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    if my_direction == K_UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)

    if my_direction == K_DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)

    if my_direction == K_RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])

    if my_direction == K_LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)

    for pos in snake:
        screen.blit(snake_skin, pos)
        if pos[0] < 0 or pos[0] > constant.GAME_WIDTH or pos[1] < 0 or pos[1] > constant.GAME_HEIGHT:
            print(constant.GAME_OVER_MESSAGE)
            pygame.quit()

    pygame.display.update()
