from collections import Counter
import scoring_param as sp

class CounterDices(Counter):

    def __hash__(self):
        return hash(tuple(sorted(self.elements())))

    def best_triple(self):
        if self[1] > 2:
            return 1
        for i in range(6, 1, -1):
            if self[i] > 2:
                return i
        return 0

    def has_straight(self):
        if self[2] and self[3] and self[4] and self[5]:
            if self[1]:
                return 1
            elif self[6]:
                return 2
        else:
            return 0

    def not_empty_point(self):
        if self[1] > 0 or self[5] > 0 or self.best_triple > 0:
            True
        else:
            False

    def all_combinations(self):
        if self.not_empty_point():
            scores_set = set()
            # top bottom recursively
            if sp.JUST_1 in self:
                scores_set.add((sp.JUST_1, 100))
                sub_set = self.subtract(sp.JUST_1).all_combinations()
                for sub_score in sub_set:
                    scores_set.add((sp.JUST_1, 
                                    100 + sub_score[1]))

            return scores_set
        else:
            return set([Counter([]), 0])
    
    def best_combination(self):
        ...

    def total_point(self):
        ...
    
if __name__ == '__main__':

    ...
    hash((1, 1, 2, 3))
    ms = set([(CounterDices([1, 5]), 150), 
            CounterDices([2, 1]), 
            (CounterDices([5, 1]), 150)])

    print(ms)
    # print(set([(1,1),(1,3),(1,1)]).union(set.union(set([(1,1),(1,2),(1,1)]))))