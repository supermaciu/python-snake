"""Logika owocu, który zwiększa wynik i wydłuża węża."""

import random

from constants import GRID_SIZE, ORANGE, WHITE
from node import Node


class Fruit(Node):
    """Reprezentuje owoc pojawiający się na planszy."""

    def __init__(self, snake):
        """Losuje pozycję owocu poza ciałem węża."""
        self.snake = snake
        self.node_size = snake.head.node_size
        self.row = random.randint(1, GRID_SIZE - 1)
        self.col = random.randint(1, GRID_SIZE - 1)

        for node in self.snake.body:
            while self.get_pos() == node.get_pos():
                self.row = random.randint(1, GRID_SIZE - 1)
                self.col = random.randint(1, GRID_SIZE - 1)

        super().__init__(self.row, self.col, ORANGE, self.node_size)

    def reset(self, score):
        """Zwiększa wynik, wydłuża węża i losuje nowy owoc."""
        self.color = WHITE
        score += 1
        print("Twój wynik: {}".format(score))

        self.snake.add_node()
        self.__init__(self.snake)
        return score
