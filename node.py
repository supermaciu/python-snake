"""Podstawowy element siatki planszy."""

import pygame

from constants import WHITE


class Node:
    """Reprezentuje jedno pole planszy gry."""

    def __init__(self, row, col, color, node_size):
        """Tworzy pole na podanej pozycji siatki."""
        self.row = row
        self.col = col
        self.node_size = node_size
        self.x = row * node_size
        self.y = col * node_size
        self.color = color

    def get_pos(self):
        """Zwraca pozycję pola w siatce."""
        return self.row, self.col

    def set_pos(self, pos):
        """Ustawia pozycję pola i przelicza współrzędne ekranu."""
        self.row, self.col = pos
        self.x = self.row * self.node_size
        self.y = self.col * self.node_size

    def reset(self):
        """Przywraca domyślny kolor pola."""
        self.color = WHITE

    def draw(self, win):
        """Rysuje pole na wskazanym oknie."""
        pygame.draw.rect(win, self.color, (self.x, self.y, self.node_size, self.node_size))
