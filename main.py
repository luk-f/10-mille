from dix_mille import DixMille
from counter_dices import CounterDices

if __name__ == '__main__':
    
    game = DixMille()
    points = game._round_player(1)
    print(f"You are making {points} points !")