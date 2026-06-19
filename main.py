"""Główny punkt startowy gry Snake."""

import pygame
import time

from config import Config
from constants import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
)
from grid import Grid
from util import draw_grid, play_random_pitch

def main():
    """Uruchamia grę, obsługuje pętlę i zapisuje wynik końcowy."""
    pygame.mixer.init()
    pygame.init()
    
    crunch_sound = pygame.mixer.Sound("crunch.mp3")
    meow_sound = pygame.mixer.Sound("meow.mp3")

    config = Config()
    screen_size = config.screen_size
    fps = config.fps
    grid_size = config.grid_size
    # move_interval = config.move_interval bedzie sie zmienial
    node_size = screen_size // grid_size

    screen = pygame.display.set_mode((screen_size, screen_size))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()

    running = True
    move_timer = 0.0
    score = 0
    grid = Grid(grid_size, node_size, config)

    while running:
        dt = clock.tick(fps) / 1000.0
        move_timer += dt

        while move_timer >= config.move_interval:
            move_timer -= config.move_interval
            running, score, ate = grid.update(score, config.high_score)
            if ate:
                play_random_pitch(crunch_sound, 0.7, 1.3)
                print("Twój wynik: {}".format(score))
            config.high_score = max(config.high_score, score)

        #     if not running:
        #         break

        # if not running:
        #     break

        screen.fill(WHITE)
        grid.draw(screen)
        draw_grid(screen, grid_size, screen_size)
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
                    grid.snake.set_direction(direction)

                if event.key == pygame.K_ESCAPE:
                    running = False

    meow_sound.play()

    grid.setup_end_animation()
    
    finished = False
    while not finished:
        dt = clock.tick(fps) / 1000.0
        
        pygame.event.pump()
        
        screen.fill(WHITE)
        grid.draw(screen)
        draw_grid(screen, grid_size, screen_size)
        pygame.display.flip()
        
        finished = grid.end_animation(dt, screen_size)

    print("GAME OVER!\n\nTwój wynik wynosił: {} | High score: {}".format(score, config.high_score))

    config.high_score = max(config.high_score, score)
    config.save()
    pygame.quit()


if __name__ == "__main__":
    main()
