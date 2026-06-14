"""Główny punkt startowy gry Snake."""

import pygame

from config import Config
from constants import (
    DEFAULT_SCREEN_SIZE,
    DOWN,
    GRID_SIZE,
    LEFT,
    MOVE_INTERVAL,
    RIGHT,
    UP,
    WHITE,
)
from fruit import Fruit
from snake import Snake
from util import draw_grid, make_grid

def main():
    """Uruchamia grę, obsługuje pętlę i zapisuje wynik końcowy."""
    pygame.init()

    config = Config()
    screen_size = config.screen_size or DEFAULT_SCREEN_SIZE
    fps = config.fps
    node_size = screen_size // GRID_SIZE

    screen = pygame.display.set_mode((screen_size, screen_size))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()

    running = True
    move_timer = 0.0
    score = 0

    grid = make_grid(GRID_SIZE, node_size)
    head = grid[int(GRID_SIZE / 2)][int(GRID_SIZE / 2)]
    snake = Snake(head, grid)
    fruit = Fruit(snake)

    try:
        while running:
            dt = clock.tick(fps) / 1000.0
            move_timer += dt

            while move_timer >= MOVE_INTERVAL:
                move_timer -= MOVE_INTERVAL
                snake.move()

                if head.row == -1:
                    head_row, head_col = head.get_pos()
                    head.set_pos((head_row + GRID_SIZE, head_col))
                    snake.direction = LEFT
                elif head.row == GRID_SIZE:
                    head_row, head_col = head.get_pos()
                    head.set_pos((head_row - GRID_SIZE, head_col))
                    snake.direction = RIGHT
                elif head.col == -1:
                    head_row, head_col = head.get_pos()
                    head.set_pos((head_row, head_col + GRID_SIZE))
                    snake.direction = UP
                elif head.col == GRID_SIZE:
                    head_row, head_col = head.get_pos()
                    head.set_pos((head_row, head_col - GRID_SIZE))
                    snake.direction = DOWN

                if snake.check_collision(score, config.high_score):
                    running = False
                    break

                if head.get_pos() == fruit.get_pos():
                    score = fruit.reset(score)
                    config.high_score = max(config.high_score, score)

            if not running:
                break

            screen.fill(WHITE)

            for row in grid:
                for node in row:
                    node.draw(screen)

            fruit.draw(screen)
            snake.draw(screen)
            draw_grid(screen, GRID_SIZE, screen_size)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    key_to_direction = {
                        pygame.K_RIGHT: RIGHT,
                        pygame.K_d: RIGHT,
                        pygame.K_LEFT: LEFT,
                        pygame.K_a: LEFT,
                        pygame.K_UP: UP,
                        pygame.K_w: UP,
                        pygame.K_DOWN: DOWN,
                        pygame.K_s: DOWN,
                    }

                    direction = key_to_direction.get(event.key)
                    if direction is not None:
                        snake.set_direction(direction)

                    if event.key == pygame.K_ESCAPE:
                        running = False
    finally:
        config.high_score = max(config.high_score, score)
        config.save()
        pygame.quit()


if __name__ == "__main__":
    main()
