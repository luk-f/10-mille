import logging

import pygame

from dix_mille import DixMille
from counter_dices import CounterDices

from graphical_object import GraphicalDice, GraphicalButton
from settings import SIZE_DICES_BOARD, SIZE_DICES_ASIDE
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
      self.dices_aside = []

      self._number_of_current_dices_on_board = 5
      self._update_board()

      self.buttons = {}
      self.buttons['shuffle'] = GraphicalButton(82.5, 145, DixMillePyGame.font.render, 
         "Shuffle", DixMillePyGame.font.size, 
         activate=False
      )
      self.buttons['put_aside'] = GraphicalButton(282.5, 145, DixMillePyGame.font.render, 
         "Put dice aside", DixMillePyGame.font.size, 
         activate=False
      )
      self.buttons['next_p'] = GraphicalButton(500.5, 145, DixMillePyGame.font.render, 
         "Next player", DixMillePyGame.font.size, 
         activate=True
      )

   def _update_board(self):
      self.dices_board = []
      start_x = 70
      for _ in range(self._number_of_current_dices_on_board):
         self.dices_board.append(GraphicalDice(start_x, 60, SIZE_DICES_BOARD))
         start_x += 120

   def update_ui(self):

      self.display.fill(WHITE)
      text = DixMillePyGame.font.render("Score", True, BLACK)
      self.display.blit(text, [320, 240])

      for dice in self.dices_board:
         dice.drawing(self.display)
      for dice in self.dices_aside:
         dice.drawing(self.display)

      for key_button in self.buttons:
         self.buttons[key_button].drawing(self.display)

      pygame.display.flip()
   
   def shuffle_dices(self):
      self._update_board()
      for _ in range(20):
         result_dices = self.game._roll_dices(self._number_of_current_dices_on_board)
         result_dices_list = result_dices.list()
         for res_i, dice in enumerate(self.dices_board):
            dice.number = result_dices_list[res_i]
         self.update_ui()
         pygame.time.wait(50)
      return result_dices

   def execute_game(self):
      self.update_ui()
      stop_game = False
      one_player_win = False

      while not one_player_win and not stop_game:
         # TODO : change by player's name
         for num_player in range(self.game._number_players):
            self.buttons['next_p'].activate = True
            while self.buttons['next_p'].activate and not stop_game:
               for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                     popup_res = self.boolean_popup("Do you want to quit game ?")
                     if popup_res:
                        stop_game = True
                  elif event.type == pygame.MOUSEBUTTONUP:
                     if self.buttons['next_p'].button.collidepoint(event.pos):
                        self.buttons['next_p'].activate = False
               self.update_ui()
            self.buttons['next_p'].activate = False
            self.buttons['shuffle'].activate = True
            logging.info(f"it's the turn of player {num_player}")
            end_player_turn = False
            point_player_turn = 0
            self._number_of_current_dices_on_board = 5
            self._update_board()
            self.update_ui()
            dices_table = None
            should_to_choose_dices = False 

            while not end_player_turn and not stop_game:
               for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                     popup_res = self.boolean_popup("Do you want to quit game ?")
                     if popup_res:
                        stop_game = True
                  elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                     if event.type == pygame.MOUSEBUTTONDOWN:
                        ...
                     elif event.type == pygame.MOUSEBUTTONUP:
                        
                        # to shuffle dices
                        if self.buttons['shuffle'].button.collidepoint(event.pos) and self.buttons['shuffle'].activate:
                              self.buttons['shuffle'].activate = False
                              dices_table = self.shuffle_dices()
                              # # DEBUG : brut force choose dices if see bug
                              # for res_i, dice in enumerate(self.dices_board):
                              #    dice.number = [1, 1, 5, 5, 4][res_i]
                              # dices_table = CounterDices([1, 1, 5, 5, 4])
                              # # DEBUG
                              logging.info(f'Dices obtained : {dices_table}')
                              # if no point, round stop with 0 point
                              if not dices_table.has_point():
                                 point_player_turn = 0
                                 end_player_turn = True
                                 self.buttons['shuffle'].activate = False
                                 self.dices_aside = []
                              else:
                                 should_to_choose_dices = True
                                 unique_combi = dices_table.all_unique_combinations()
                                 logging.debug(unique_combi)
                                 dices_chosen = CounterDices()

                        # choose one or more dices
                        if dices_table and should_to_choose_dices:
                           for id, dice in enumerate(self.dices_board):
                                 if dice.rect.collidepoint(event.pos):
                                    logging.debug(f"Dice {id} touched")
                                    if not dice.selected:
                                       dices_chosen[dice.number] += 1
                                    else:
                                       dices_chosen[dice.number] -= 1
                                    dice.selected = not dice.selected
                           logging.debug(dices_chosen)
                           if dices_chosen.has_point() and dices_chosen.test_if_contains_only_combination():
                              logging.debug(dices_chosen.best_combination())
                              self.buttons['put_aside'].activate = True
                           else:
                              self.buttons['put_aside'].activate = False

                        # put dice aside
                        if self.buttons['put_aside'].button.collidepoint(event.pos) and self.buttons['put_aside'].activate:
                           
                           self.buttons['put_aside'].activate = False
                           should_to_choose_dices = False
                           for id, dice in enumerate(self.dices_board):
                              if dice.selected:
                                 dice.selected = False
                           
                           start_x = 42
                           start_x += 72 * len(self.dices_aside)
                           number_of_dice_put_aside = 0
                           for dice_number, ite_dice in dices_chosen.best_combination().combination_of_dices().items():
                              for _ in range(ite_dice):
                                 g_dice = GraphicalDice(start_x, 300, SIZE_DICES_ASIDE)
                                 g_dice.number = dice_number
                                 self.dices_aside.append(g_dice)
                                 start_x += 72
                                 number_of_dice_put_aside += 1

                           if number_of_dice_put_aside > 0:
                              self.buttons['shuffle'].activate = True
                              self._number_of_current_dices_on_board -= number_of_dice_put_aside
                              if self._number_of_current_dices_on_board == 0:
                                 self._number_of_current_dices_on_board = 5
                                 self.dices_aside = []
                           self._update_board()

                  self.update_ui()   
                  if stop_game:
                     logging.debug(f'call break 2')
                     break
            if stop_game:
               logging.debug(f'call break 1')
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

   def __del__(self):
      pygame.quit()