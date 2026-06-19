"""Abstrakcyjna reprezentacja elementu planszy."""

from abc import ABC, abstractmethod
from pygame import Vector2


class Node(ABC):
    """Reprezentuje obiekt mający pozycję na planszy."""

    def __init__(self, row, col, color, node_size):
        """Tworzy obiekt na podanej pozycji siatki."""
        self.row = row
        self.col = col
        self.node_size = node_size
        self.x = row * node_size
        self.y = col * node_size
        self.color = color

    def get_pos(self):
        """Zwraca pozycję obiektu w siatce."""
        return self.row, self.col

    def set_pos(self, pos):
        """Ustawia pozycję obiektu i przelicza współrzędne ekranu."""
        self.row, self.col = pos
        self.x = self.row * self.node_size
        self.y = self.col * self.node_size

    @abstractmethod
    def draw(self, win):
        """Rysuje obiekt na wskazanym oknie."""
