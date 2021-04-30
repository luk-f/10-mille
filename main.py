import logging

from dix_mille import DixMille
from counter_dices import CounterDices
from dix_mille_pygame import DixMillePyGame

from settings import WHITE

import pygame

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    
    game = DixMille()
    # points = game._round_player(1)
    # print(f"You are making {points} points !")

    my_pygame = DixMillePyGame()
    my_pygame.execute_game()
