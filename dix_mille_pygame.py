import pygame

from dix_mille import DixMille
from graphical_object import GraphicalDice, GraphicalButton
from settings import SIZE_DICES_BOARD
from settings import BLACK, WHITE, RED

pygame.init()
font = pygame.font.Font('arial.ttf', 25)
clock = pygame.time.Clock()


class DixMillePyGame:

   def __init__(self, w=640, h=480):

      self.game = DixMille()

      self.w = w
      self.h = h
      self.display = pygame.display.set_mode((self.w, self.h))
      pygame.display.set_caption('10 MILLE')

      self.dices_board = []

      self._number_of_current_dices_on_board = 5
      self._update_board()

   def _update_board(self):
      self.dices_board = []
      start_x = 70
      for dice_number in range(self._number_of_current_dices_on_board):
         self.dices_board.append(GraphicalDice(start_x, 60, SIZE_DICES_BOARD))
         start_x += 120

   def update_ui(self):

      self.display.fill(WHITE)
      text = font.render("Score", True, BLACK)
      self.display.blit(text, [320, 240])
      for dice in self.dices_board:
         dice.drawing(self.display)

      self.shuffle_button = GraphicalButton(0, 0, font.render, "Shuffle").drawing(self.display)

      pygame.display.flip()
   
   def shuffle_dices(self):
      self._update_board()
      for _ in range(20):
         result_dices = self.game._roll_dices(5).list()
         for res_i, dice in enumerate(self.dices_board):
            dice.number = result_dices[res_i]
         self.update_ui()
         pygame.time.wait(50)

if __name__ == '__main__':

   my_pygame = DixMillePyGame()
   my_pygame.display.fill(WHITE)
   # dice_6 = GraphicalDice(180, 180, 5)
   # dice_6.drawing(my_pygame.display, 6)

   my_pygame.update_ui()

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
               ...
            elif event.type == pygame.MOUSEBUTTONUP:
               if my_pygame.shuffle_button.collidepoint(event.pos):
                  my_pygame.shuffle_dices()
               for id, dice in enumerate(my_pygame.dices_board):
                  if dice.rect.collidepoint(event.pos):
                     print(f"Dice {id} touched")
                     dice.selected = not dice.selected 
               my_pygame.update_ui()
               
      if stop:
         break
      clock.tick(60)
   