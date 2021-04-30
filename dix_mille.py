import logging

import dice
from player import PlayerDixMille
from counter_dices import CounterDices
from combination import _Combination
from combinations_tuple import CombinationsTuple


def ask_choose_combination(total_combination: int) -> int:
    choice = None
    while choice is None:
        selected = input('\tWhich combinaison ? ')
        try:
            selected = int(selected)
            if 0 <= selected < total_combination:
                choice = selected
            else:
                logging.info(f"\tChoose between 0 and {total_combination-1}")
        except:
            logging.info("\tChoose natural number")
    return choice

def count_points_in_combination_list(combination_list : CombinationsTuple) -> int:
    sum_of_points = 0
    for combi in combination_list:
        sum_of_points += combi.score
    return sum_of_points

class DixMille:

    best_rank = 1

    def __init__(self, number_of_players: int = 2):
        
        self._number_players = number_of_players
        # init dict of players
        self._players_dict = {}
        # fill dict of players
        for i in range(self._number_players):
            # tmp_name = input(f"What is the name of the player {i} ?")
            tmp_name = f"J n°{i}"
            tmp_player = PlayerDixMille(tmp_name)
            self._players_dict[tmp_player.get_id()] = tmp_player

    def _roll_dices(self, number_of_dices: int = 5):
        return CounterDices(dice.roll(f'{number_of_dices}d6'))

    def _round_table(self):
        ...

    def _choose_dices(self, dices_table):
        dices_aside = False

    def _round_player(self, player_id):
        """
        Round for a player. Can roll dices as long as he obtain points.
        """
        combination_dices_aside = CombinationsTuple()
        combination_dices_aside_total = CombinationsTuple()
        number_of_dices = 5
        while True:
            # if player has put all dices aside
            if number_of_dices == 0:
                combination_dices_aside_total.extend(combination_dices_aside)
                combination_dices_aside = []
                number_of_dices = 5
            # Roll dices
            dices_table = self._roll_dices(number_of_dices)
            logging.info(f'Dices obtained : {dices_table}')
            # if no point, round stop with 0 point
            if not dices_table.has_point():
                return 0
            dices_aside = False
            while dices_table.has_point():
                logging.info("\tGreat ! There are points !")
                unique_combi = dices_table.all_unique_combinations()
                if len(unique_combi) == 1 and not dices_aside:
                    logging.info("\tNo choice, first combination selected.")
                    combi_selected = unique_combi.pop()
                    logging.info(f"\t{combi_selected}")
                elif self._players_dict[player_id].is_human():
                    unique_combi_dict = {}
                    c_num = 0
                    for c_dice in unique_combi:
                        unique_combi_dict[c_num] = c_dice
                        logging.info(f'\t - ({c_num}) -> {c_dice}')
                        c_num += 1
                    if dices_aside:
                        unique_combi_dict[c_num] = _Combination()
                        logging.info(f'\t - ({c_num}) -> Reroll {len(dices_table)} dice(s)')
                        c_num += 1
                    selected = ask_choose_combination(c_num)
                    combi_selected = unique_combi_dict[selected]
                else:
                    logging.info("You are a robot.")
                combination_dices_aside.append(combi_selected)
                dices_aside = True
                dices_table -= combi_selected._combi
                number_of_dices = len(list(dices_table.elements()))
                if len(combi_selected._combi) == 0:
                    break
            choice = None
            while choice is None:
                logging.info('You took all points.')
                res = input('Do you want stop your round ? (y/n) ')
                if res == 'y' or res == 'n':
                    choice = res
                else:
                    logging.info(f"\tDon't understand...")
            if choice == 'y':
                combination_dices_aside_total.extend(combination_dices_aside)
                return count_points_in_combination_list(combination_dices_aside_total)

    def _count_point(self, dices_counter: CounterDices):
        ...
        point = 0
        while dices_counter > 2 or (dices_counter.count(1) or dices_counter.count(5)):
            if dices_counter.count(3):
                point += 1_000
                