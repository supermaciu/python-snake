"""Logika ruchu, wzrostu i kolizji węża."""

import time

import pygame

from constants import DARK_GREEN, DOWN, GREEN, LEFT, RIGHT, UP
from node import Node


class Snake:
    """Steruje ruchem węża oraz jego stanem."""

    def __init__(self, head, grid):
        """Tworzy węża na bazie głowy i siatki pól."""
        self.starting_nodes = 3
        self.grid = grid
        self.head = head
        self.body = [head]
        head_row, head_col = head.get_pos()

        for i in range(1, self.starting_nodes):
            self.body.append(grid[head_row - i][head_col])

        self.color = GREEN
        self.direction = RIGHT
        self.direction_locked = False

    def _is_opposite(self, direction):
        """Sprawdza, czy nowy kierunek jest przeciwny do aktualnego."""
        return (
            self.direction[0] + direction[0] == 0
            and self.direction[1] + direction[1] == 0
        )

    def set_direction(self, direction):
        """Ustawia nowy kierunek, jeśli jest dozwolony."""
        if self.direction_locked:
            return

        if direction == self.direction or self._is_opposite(direction):
            return

        self.direction = direction
        self.direction_locked = True

    def add_node(self):
        """Dodaje nowy segment na końcu węża."""
        last_node = self.body[-1]
        last_node_row, last_node_col = last_node.get_pos()
        self.body.append(Node(last_node_row, last_node_col, self.color, last_node.node_size))

    def move(self):
        """Przesuwa ciało węża o jedno pole."""
        self.old_body = self.body.copy()

        for i in range(len(self.body) - 1, 0, -1):
            old_node = self.old_body[i - 1]
            self.body[i].set_pos(old_node.get_pos())

        head_row, head_col = self.head.get_pos()
        self.head.set_pos((head_row + self.direction[0], head_col + self.direction[1]))
        self.direction_locked = False

    def check_collision(self, score, high_score):
        """Sprawdza kolizję głowy z ciałem i wypisuje wynik."""
        for node in self.body[1:]:
            if self.head.get_pos() == node.get_pos():
                print(
                    "GAME OVER!\n\nTwój wynik wynosił: {} | High score: {}".format(
                        score, high_score
                    )
                )
                time.sleep(1)
                return True

        return False

    def draw(self, win):
        """Rysuje ciało i głowę węża."""
        for node in self.body[1:]:
            pygame.draw.rect(win, self.color, (node.x, node.y, node.node_size, node.node_size))
        pygame.draw.rect(
            win, DARK_GREEN, (self.head.x, self.head.y, self.head.node_size, self.head.node_size)
        )
