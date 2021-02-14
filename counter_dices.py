from collections import Counter

class CounterDices(Counter):

    def best_triple(self):
        if self[1] > 2:
            return 1
        for i in range(6, 1, -1):
            if self[i] > 2:
                return i
        return 0

    def not_empty_point(self):
        if self[1] > 0 or self[5] > 0 or self.best_triple > 0:
            True
        else:
            False
    
    def best_combination(self):
        ...

    def total_point(self):
        ...
    
