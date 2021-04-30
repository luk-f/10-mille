import sys
from typing import List, Tuple

import pygame
from settings import BLACK, RED, BLUE1, BLUE2, GRAY1, GRAY2

if sys.version_info < (3,9):
   Coordinate = Tuple[float, float]
   ListCoord = List[Coordinate]
else:
   Coordinate = tuple[float, float]
   ListCoord = list[Coordinate]

class GraphicalButton:

    def __init__(self, x, y, font_render, text, font_size,
                 width=None, activate: bool = True):
        self._x = x
        self._y = y
        self._font_render = font_render
        self._font_size = font_size
        self._text = text
        self._text_size = self._font_size(self._text)
        self._width = self._text_size[0] + 20
        self._activate = activate

    @property
    def activate(self) -> bool:
        return self._activate

    @activate.setter
    def activate(self, activate: bool):
        self._activate = activate

    def _define_color_activation(self):

        if self._activate:
            self.color1 = BLUE1
            self.color2 = BLUE2
        else:
            self.color1 = GRAY1
            self.color2 = GRAY2

    def drawing(self, current_display) -> pygame.draw.rect:

        self._define_color_activation()

        # external rectangle
        pygame.draw.rect(current_display, self.color1, 
            pygame.Rect(self._x - self._width/2, self._y - 25, 
                self._width, 50), 0, 15)

        # internal rectangle
        self.button = pygame.draw.rect(current_display, self.color2, 
            pygame.Rect(self._x - self._width/2 + 5, self._y - 20,
                self._width - 10, 40), 0, 10)

        # text
        text = self._font_render(self._text, True, BLACK)
        current_display.blit(text, [self._x - self._text_size[0]/2, self._y - 15])

        return self.button


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