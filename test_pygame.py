import sys
from typing import List, Tuple
import pygame

pygame.init()
font = pygame.font.Font('arial.ttf', 25)
clock = pygame.time.Clock()

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLUE3 = (100, 100, 255)

if sys.version_info < (3,9):
   Coordinate = Tuple[float, float]
   ListCoord = List[Coordinate]
else:
   Coordinate = tuple[float, float]
   ListCoord = list[Coordinate]

class GraphicalDice:

   def __init__(self, x, y, size):
      self.x = x
      self.y = y
      self.size = size
      self._number = None
      self.dots_list = ListCoord

   def _define_dots_position_by_number(self):
      if self._number:
         if self._number in [1, 3, 5]:
            self.dots_list = [(self.x, self.y)]
            if self._number in [3, 5]:
               self.dots_list.append((self.x-(20*self.size)*0.2, self.y-(20*self.size)*0.2))
               self.dots_list.append((self.x+(20*self.size)*0.2, self.y+(20*self.size)*0.2))
               if self._number == 5:
                  self.dots_list.append((self.x+(20*self.size)*0.2, self.y-(20*self.size)*0.2))
                  self.dots_list.append((self.x-(20*self.size)*0.2, self.y+(20*self.size)*0.2))
         elif self._number in [2, 4]:
            self.dots_list = [(self.x-(20*self.size)*0.15, self.y-(20*self.size)*0.15), \
               (self.x+(20*self.size)*0.15, self.y+(20*self.size)*0.15)]
            if self._number == 4:
               self.dots_list.append((self.x-(20*self.size)*0.15, self.y+(20*self.size)*0.15))
               self.dots_list.append((self.x+(20*self.size)*0.15, self.y-(20*self.size)*0.15))
         elif self._number == 6:
            self.dots_list = [(self.x-(20*self.size)*0.15, self.y-(20*self.size)*0.25), \
               (self.x-(20*self.size)*0.15, self.y), \
               (self.x-(20*self.size)*0.15, self.y+(20*self.size)*0.25), \
               (self.x+(20*self.size)*0.15, self.y-(20*self.size)*0.25), \
               (self.x+(20*self.size)*0.15, self.y), \
               (self.x+(20*self.size)*0.15, self.y+(20*self.size)*0.25)]

   @property
   def number(self):
      return self._number

   @number.setter
   def number(self, number):
      self._number = number
      self._define_dots_position_by_number()

   def drawing(self, current_display, number=None):
      if number:
         self.number = number
      """draw outline"""
      pygame.draw.rect(current_display, BLACK, 
         pygame.Rect(self.x-(20*self.size)/2, self.y-(20*self.size)/2, 
            20*self.size, 20*self.size),
         self.size, 4*self.size)
      """draw dots"""
      if self.number:
         for dot_x, dot_y in self.dots_list:
            pygame.draw.circle(current_display, BLACK, 
               (dot_x, dot_y), 2*self.size)


class DixMillePyGame:

   def __init__(self, w=640, h=480):
      self.w = w
      self.h = h
      self.display = pygame.display.set_mode((self.w, self.h))
      pygame.display.set_caption('10 MILLE')

      self.dices_table = [GraphicalDice(60, 60, 5),\
         GraphicalDice(180, 60, 5),\
         GraphicalDice(300, 60, 5),\
         GraphicalDice(420, 60, 5),\
         GraphicalDice(540, 60, 5)]

   def _update_ui(self):
      self.display.fill(WHITE)
      text = font.render("Score", True, BLACK)
      self.display.blit(text, [320, 240])

      for dice in self.dices_table:
         dice.drawing(self.display)

      pygame.draw.rect(self.display, BLUE1, 
         pygame.Rect(20, 120, 100, 50), 0, 0)
      pygame.draw.polygon(self.display, BLUE2, 
         [(20, 170), (120, 170), (120, 120)])
      pygame.draw.rect(self.display, BLUE3, 
         pygame.Rect(30, 130, 80, 30), 0, 0)

      pygame.display.flip()

if __name__ == '__main__':

   my_pygame = DixMillePyGame()
   my_pygame.display.fill(WHITE)
   # dice_1 = GraphicalDice(60, 60, 5)
   # dice_1.drawing(my_pygame.display, 1)
   # dice_2 = GraphicalDice(180, 60, 5)
   # dice_2.drawing(my_pygame.display, 2)
   # dice_3 = GraphicalDice(300, 60, 5)
   # dice_3.drawing(my_pygame.display, 3)
   # dice_4 = GraphicalDice(420, 60, 5)
   # dice_4.drawing(my_pygame.display, 4)
   # dice_5 = GraphicalDice(60, 180, 5)
   # dice_5.drawing(my_pygame.display, 5)
   # dice_6 = GraphicalDice(180, 180, 5)
   # dice_6.drawing(my_pygame.display, 6)

   my_pygame._update_ui()

   stop = False
   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            stop = True
         elif event.type == pygame.MOUSEWHEEL:
            print(event)
            print(event.x, event.y)
            print(event.flipped)
            print(event.which)
            # can access properties with
            # proper notation(ex: event.y)
         elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
            if event.type == pygame.MOUSEBUTTONDOWN:
               print(event)
            elif event.type == pygame.MOUSEBUTTONUP:
               print(event)

      if stop:
         break
      clock.tick(60)
   