import logging

import pygame

from dix_mille import DixMille
from graphical_object import GraphicalDice, GraphicalButton
from settings import SIZE_DICES_BOARD
from settings import BLACK, WHITE, RED


class DixMillePyGame:

   pygame.init()
   font = pygame.font.Font('arial.ttf', 25)
   clock = pygame.time.Clock()

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
      text = DixMillePyGame.font.render("Score", True, BLACK)
      self.display.blit(text, [320, 240])

      for dice in self.dices_board:
         dice.drawing(self.display)

      self.shuffle_button = GraphicalButton(82.5, 145, DixMillePyGame.font.render, 
         "Shuffle", DixMillePyGame.font.size).drawing(self.display)

      pygame.display.flip()
   
   def shuffle_dices(self):
      self._update_board()
      for _ in range(20):
         result_dices = self.game._roll_dices(5).list()
         for res_i, dice in enumerate(self.dices_board):
            dice.number = result_dices[res_i]
         self.update_ui()
         pygame.time.wait(50)

   def execute_game(self):
      self.update_ui()
      stop = False
      while True:
         for event in pygame.event.get():
               if event.type == pygame.QUIT:
                  popup_res = self.boolean_popup("Do you want to quit game ?")
                  if popup_res:
                     pygame.quit()
                     stop = True
                     break
               elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                  if event.type == pygame.MOUSEBUTTONDOWN:
                     ...
                  elif event.type == pygame.MOUSEBUTTONUP:
                     if self.shuffle_button.collidepoint(event.pos):
                           self.shuffle_dices()
                     for id, dice in enumerate(self.dices_board):
                           if dice.rect.collidepoint(event.pos):
                              logging.debug(f"Dice {id} touched")
                              dice.selected = not dice.selected
               self.update_ui()
                  
         if stop:
               break
         DixMillePyGame.clock.tick(60)


   def boolean_popup(self, message: str):

      self.display.fill(WHITE)
      pygame.display.set_caption(message)
      
      text = DixMillePyGame.font.render(message, True, BLACK)
      self.display.blit(text, [150, 30])

      yes_button = GraphicalButton(250, 100, 
            DixMillePyGame.font.render, "Yes", 
            DixMillePyGame.font.size).\
         drawing(self.display)
      no_button = GraphicalButton(370, 100, 
            DixMillePyGame.font.render, "No", 
            DixMillePyGame.font.size).\
         drawing(self.display)

      pygame.display.flip()

      while True:
         for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                  logging.debug(event)
                  if yes_button.collidepoint(event.pos):
                     return True
                  if no_button.collidepoint(event.pos):
                     return False
            elif event.type == pygame.QUIT:
                  return False
         DixMillePyGame.clock.tick(60)

   