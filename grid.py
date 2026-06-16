"""Zarządzanie stanem planszy, wężem i owocem."""

import random

from fruit import Fruit
from snake import Snake
from constants import *


class Grid:
    """Łączy logikę planszy z obiektami gry."""

    def __init__(self, grid_size, node_size, config):
        """Tworzy planszę z jednym wężem i jednym owocem."""
        self.config = config
        
        self.grid_size = grid_size
        self.node_size = node_size
        self.snake = Snake(grid_size, node_size)
        self.fruit = Fruit(node_size)
        self.place_fruit_random()

    def get_occupied_positions(self):
        """Zwraca zbiór pól zajętych przez węża."""
        return {node.get_pos() for node in self.snake.body}

    def place_fruit_random(self):
        """Ustawia owoc na losowym wolnym polu planszy."""
        all_positions = [
            (row, col)
            for row in range(self.grid_size)
            for col in range(self.grid_size)
        ]
        occupied_positions = self.get_occupied_positions()
        free_positions = [pos for pos in all_positions if pos not in occupied_positions]

        if not free_positions:
            return False

        self.fruit.set_pos(random.choice(free_positions))
        return True

    def __wrap_head(self):
        """Zawija głowę węża na przeciwległą stronę planszy."""
        head_row, head_col = self.snake.head.get_pos()
        wrapped_row = head_row % self.grid_size
        wrapped_col = head_col % self.grid_size
        self.snake.head.set_pos((wrapped_row, wrapped_col))

    def update(self, score, high_score):
        """Wykonuje jeden krok logiki i zwraca stan gry oraz wynik."""
        self.snake.move()
        self.__wrap_head()

        ate = False

        if self.snake.check_collision(score, high_score):
            self.snake.head.color = RED
            return False, score, ate

        if self.snake.head.get_pos() == self.fruit.get_pos():
            score += 1
            ate = True
            
            self.snake.add_node()
            self.place_fruit_random()
            
            # utrudnienie
            self.config.move_interval -= 0.001 if self.config.move_interval > 0.05 else 0

        return True, score, ate

    def draw(self, win):
        """Rysuje obiekty gry na planszy."""
        self.fruit.draw(win)
        self.snake.draw(win)
