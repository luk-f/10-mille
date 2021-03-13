from collections import Counter

from combinations_tuple import CombinationsTuple
from combination import ALL_CBNT

class CounterDices(Counter):

    def __hash__(self):
        return hash(tuple(sorted(self.elements())))

    def has_point(self) -> bool:
        if self[1] > 0 or self[5] > 0:
            return True
        elif self:
            if self.most_common(1)[0][1] > 2:
                return True
        return False

    def all_unique_combinations(self) -> set():
        combinations_set = set()
        for each_cb in ALL_CBNT:
            if each_cb._combi & self == each_cb._combi:
                combinations_set.add(each_cb)
        return combinations_set

    # def all_unique_combinations_in_dict(self) -> dict:
    #     combi_set = self.all_unique_combinations()
    #     combi_dict = {}
    #     combi_number = 0
    #     while combi_set:
    #         combi_dict[combi_number] = combi_set.pop()
    #         combi_number += 1
    #     return combi_dict

    def all_combinations(self) -> set:
        if self.has_point():
            scores_set = set()
            ct_set = self.all_unique_combinations()
            while ct_set:
                each_cb = ct_set.pop()
                scores_set.add(CombinationsTuple([each_cb]))
                # top bottom recursively
                sub_ct_set = CounterDices(self - each_cb._combi).all_combinations()
                while sub_ct_set:
                    scores_set.add(CombinationsTuple([each_cb]) +
                                    sub_ct_set.pop())
            return scores_set
        else:
            return set()
    
    def best_combination(self):
        ...

    def total_point(self):
        ...

    def __repr__(self):
        return f'{list(self.elements())}'
    
from combination import _HashIntCounter as HIC

if __name__ == '__main__':

    ...
    my_cd = CounterDices([1, 1, 3, 4, 5])
    my_hic = HIC([1])
    print(my_cd)
    print(my_hic)
    print(my_cd - my_hic)