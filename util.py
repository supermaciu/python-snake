"""Funkcje pomocnicze dla planszy gry."""

import pygame
from constants import GREY

def draw_grid(win, rows, width):
    """Rysuje linie siatki na planszy."""
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))
