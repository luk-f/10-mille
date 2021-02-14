from dix_mille import DixMille
from scoring_param import COMBINATIONS
from counter_dices import CounterDices

if __name__ == '__main__':
    
    game = DixMille()
    # print(game._roll_dices())
    # print(game._roll_dices(3))
    # print(COMBINATIONS['suite_1'])
    for _ in range(100):
        c_dices = CounterDices(game._roll_dices())
        print()
        print(c_dices)
        print(c_dices.best_triple())
