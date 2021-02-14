import dice
from player import PlayerDixMille
from counter_dices import CounterDices

class DixMille():

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

    def _round_player(self, player_id):
        dices_aside = []
        dices_table = self._roll_dices()
        while True:
            ...

    def _count_point(self, dices_counter: CounterDices):
        ...
        point = 0
        while dices_counter > 2 or (dices_counter.count(1) or dices_counter.count(5)):
            if dices_counter.count(3):
                point += 1_000
                