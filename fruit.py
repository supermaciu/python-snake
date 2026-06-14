"""Logika owocu, który zwiększa wynik i wydłuża węża."""

import pygame

from constants import ORANGE
from node import Node


class Fruit(Node):
    """Reprezentuje czerwony/pomarańczowy owoc."""

    def __init__(self, node_size):
        """Tworzy owoc na planszy."""
        super().__init__(0, 0, ORANGE, node_size)

    def draw(self, win):
        """Rysuje owoc na planszy."""
        pygame.draw.rect(win, self.color, (self.x, self.y, self.node_size, self.node_size))
