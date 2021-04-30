import sys

from typing import List
from combination import _Combination
from collections import Counter

if sys.version_info < (3,9):
    ListCombinations = List[_Combination]
else:
    ListCombinations = list[_Combination]

class CombinationsTuple(ListCombinations):
    """
    Contient une liste de combinaisons
    """

    def __init__(self, list_combi: ListCombinations = None) -> None:
        if list_combi is None:
            super().__init__()
        else:
            super().__init__(list_combi)

    def total_score(self) -> int:
        return sum([x._score for x in self])

    def number_of_dices(self) -> int:
        return sum([x.count_dices() for x in self])

    def combination_of_dices(self) -> Counter:
        new_counter = Counter()
        for x in self:
            new_counter += x._combi
        return new_counter

    def __add__(self, ct_right):
        return CombinationsTuple(super().__add__(ct_right))

    def __eq__(self, ct_right) -> bool:
        if self.combination_of_dices() == ct_right.combination_of_dices() \
                 and self.total_score() == ct_right.total_score():
            return True
        else:
            return False
    
    
    def __lt__(self, c_right) -> bool:
        if self.total_score() < c_right.total_score():
            return True
        elif self.total_score() == c_right.total_score() \
                and self.number_of_dices() > c_right.number_of_dices():
            return True
        else:
            return False

    def __hash__(self):
        return hash(tuple(sorted(self)))