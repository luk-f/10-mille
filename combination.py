from typing import Counter

IntCounter = Counter[int]

class _HashIntCounter(IntCounter):
    
    # def __hash__(self):
    #     return hash(tuple(sorted(self.elements())))
    ...

class _Combination:
    """
    Class privée de combinaison pour recenser toutes les combinaisons de scores
    N'ont pas a être modifié au cours d'une partie.
    """

    def __init__(self, combi_list: list = [], score: int = 0) -> None:
        self._combi = _HashIntCounter(combi_list)
        self._score = score

    def __str__(self) -> str:
        return f'{self._combi} -> {self._score} pts'

    def __repr__(self) -> str:
        return f'{self._combi} -> {self._score} pts'

    def __lt__(self, c_right) -> bool:
        """
        plus petit si 
         - score plus petit
         - score équivalent mais plus de dés
        """
        if self._score < c_right._score:
            return True
        elif self._score == c_right._score and len(self._combi) > len(c_right._combi):
            return True
        else:
            return True


"""
Listes des combinaisons
"""
SUITE_1 = _Combination([1, 2, 3, 4, 5], 1000)
SUITE_2 = _Combination([2, 3, 4, 5, 6], 1000)
TRIPLE_1 = _Combination([1]*3, 1000)
TRIPLE_6 = _Combination([6]*3, 600)
TRIPLE_5 = _Combination([5]*3, 500)
TRIPLE_4 = _Combination([4]*3, 400)
TRIPLE_3 = _Combination([3]*3, 300)
TRIPLE_2 = _Combination([2]*3, 200)
JUST_1 = _Combination([1], 100)
JUST_5 = _Combination([5], 50)