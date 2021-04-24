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

    def __init__(self, x, y, font_render, text, font_size, width=None):
        self._x = x
        self._y = y
        self._font_render = font_render
        self._font_size = font_size
        self._text = text
        self._length_text = len(self._text)
        self._state = True

        if width:
            self._width = self.width
        else:
            self._width = self._length_text*15

    @property
    def state(self) -> bool:
        return self._state

    @state.setter
    def state(self, state: bool):
        self._state = state

    def drawing(self, current_display) -> pygame.draw.rect:

        # external rectangle
        pygame.draw.rect(current_display, BLUE1, 
            pygame.Rect(self._x - self._length_text*7.5, self._y - 25, 
                self._width, 50), 0, 15)

        # internal rectangle
        button = pygame.draw.rect(current_display, BLUE2, 
            pygame.Rect(self._x - self._length_text*7.5 + 5, self._y - 20,
                self._width*0.9, 40), 0, 10)

        # text
        text = self._font_render(self._text, True, BLACK)
        text_size = self._font_size(self._text)
        current_display.blit(text, [self._x - text_size[0]/2, self._y - 15])

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