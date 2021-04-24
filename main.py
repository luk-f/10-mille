from dix_mille import DixMille
from counter_dices import CounterDices
from dix_mille_pygame import DixMillePyGame

from settings import WHITE

import pygame

pygame.init()
arial_font = pygame.font.Font('arial.ttf', 25)
clock = pygame.time.Clock()

if __name__ == '__main__':
    
    game = DixMille()
    # points = game._round_player(1)
    # print(f"You are making {points} points !")

    print(game._roll_dices())

    my_pygame = DixMillePyGame()
    my_pygame.display.fill(WHITE)

    my_pygame.update_ui()

    stop = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                popup_res = my_pygame.boolean_popup("Do you want to quit game ?")
                if popup_res:
                    pygame.quit()
                    stop = True
                    break
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