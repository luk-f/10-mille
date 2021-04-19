import sys
from typing import List, Tuple

import pygame
from settings import BLACK, RED, BLUE1, BLUE2

if sys.version_info < (3,9):
   Coordinate = Tuple[float, float]
   ListCoord = List[Coordinate]
else:
   Coordinate = tuple[float, float]
   ListCoord = list[Coordinate]

class GraphicalButton:

    def __init__(self, x, y, font_render, text):
        self._x = x
        self._y = y
        self._font_render = font_render
        self._text = text
        self._state = True

    @property
    def state(self) -> bool:
        return self._state

    @state.setter
    def state(self, state: bool):
        self._state = state

    def drawing(self, current_display) -> pygame.draw.rect:

        pygame.draw.rect(current_display, BLUE1, 
            pygame.Rect(20, 120, 100, 50), 0, 5)

        button = pygame.draw.rect(current_display, BLUE2, 
            pygame.Rect(25, 125, 90, 40), 0, 5)

        text = self._font_render(self._text, True, BLACK)
        current_display.blit(text, [30, 130])

        return button


class GraphicalDice:

    def __init__(self, x, y, size):
        self._x = x
        self._y = y
        self.size = size
        self._number = None
        self.dots_list = ListCoord
        self.selected = False

    def _define_dots_position_by_number(self):
        if self._number:
            if self._number in [1, 3, 5]:
                self.dots_list = [(self._x, self._y)]
                if self._number in [3, 5]:
                    self.dots_list.append((self._x-(20*self.size)*0.2, self._y-(20*self.size)*0.2))
                    self.dots_list.append((self._x+(20*self.size)*0.2, self._y+(20*self.size)*0.2))
                if self._number == 5:
                    self.dots_list.append((self._x+(20*self.size)*0.2, self._y-(20*self.size)*0.2))
                    self.dots_list.append((self._x-(20*self.size)*0.2, self._y+(20*self.size)*0.2))
            elif self._number in [2, 4]:
                self.dots_list = [(self._x-(20*self.size)*0.15, self._y-(20*self.size)*0.15), \
                    (self._x+(20*self.size)*0.15, self._y+(20*self.size)*0.15)]
                if self._number == 4:
                    self.dots_list.append((self._x-(20*self.size)*0.15, self._y+(20*self.size)*0.15))
                    self.dots_list.append((self._x+(20*self.size)*0.15, self._y-(20*self.size)*0.15))
            elif self._number == 6:
                self.dots_list = [(self._x-(20*self.size)*0.15, self._y-(20*self.size)*0.25), \
                    (self._x-(20*self.size)*0.15, self._y), \
                    (self._x-(20*self.size)*0.15, self._y+(20*self.size)*0.25), \
                    (self._x+(20*self.size)*0.15, self._y-(20*self.size)*0.25), \
                    (self._x+(20*self.size)*0.15, self._y), \
                    (self._x+(20*self.size)*0.15, self._y+(20*self.size)*0.25)]

    @property
    def number(self) -> int:
        return self._number

    @number.setter
    def number(self, number: int):
        self._number = number
        self._define_dots_position_by_number()

    def drawing(self, current_display, number=None):
        color_selected = BLACK
        if self.selected:
            color_selected = RED
        if number:
            self.number = number
        """draw outline"""
        self.rect = pygame.draw.rect(current_display, color_selected, 
            pygame.Rect(self._x-(20*self.size)/2, self._y-(20*self.size)/2, 
                20*self.size, 20*self.size),
            self.size, 4*self.size)
        """draw dots"""
        if self.number:
            for dot_x, dot_y in self.dots_list:
                pygame.draw.circle(current_display, BLACK, 
                (dot_x, dot_y), 2*self.size)