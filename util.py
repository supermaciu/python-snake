"""Funkcje pomocnicze dla planszy gry."""

import pygame

from constants import GREY, WHITE
from node import Node


def make_grid(rows, node_size):
    """Tworzy dwuwymiarową siatkę pól gry."""
    grid = []

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, WHITE, node_size)
            grid[i].append(node)

    return grid


def draw_grid(win, rows, width):
    """Rysuje linie siatki na planszy."""
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))
