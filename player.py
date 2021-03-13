
class PlayerDixMille():
    
    player = 0

    def __init__(self, name: str = "", human: bool = True):

        self._player_number = PlayerDixMille.player
        PlayerDixMille.player += 1
        if not name:
            self._name = f"player {self._player_number}"
        else:
            self._name = name
        self._score_game = 0
        self._human = human

    def get_id(self) -> int:
        return self._player_number

    def get_name(self) -> str:
        return self._name

    def get_score(self) -> int:
        return self._score_game

    def is_human(self) -> bool:
        return self._human

    def add_value_to_score(self, value):
        if self._score_game + value <= 10_000:
            self._score_game += value
        else:
            print(f"Not possible to add {value}, overflow !")
