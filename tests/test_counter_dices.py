import unittest
from counter_dices import CounterDices

class TestCombinationsTuple(unittest.TestCase):

    def test_empty_point_or_not(self):
        c_dices = CounterDices([1, 2, 3, 4, 5])
        assert c_dices.has_point() is True, "devrait être true"
        c_dices = CounterDices([2, 2, 2, 3, 4])
        assert c_dices.has_point() is True, "devrait être true"
        c_dices = CounterDices([2, 3, 2, 3, 4])
        assert c_dices.has_point() is False, "devrait être false"
        c_dices = CounterDices()
        assert c_dices.has_point() is False, "devrait être false"

    def test_all_combinations(self):
        c_dices = CounterDices([1, 2, 2, 2, 5])
        assert len(c_dices.all_combinations()) == 7, "devrait retourner 7 solutions"
        all_combi = c_dices.all_combinations()
        assert sorted([x.number_of_dices() for x in all_combi]) == [1, 1, 2, 3, 4, 4, 5]
        assert sorted([x.total_score() for x in all_combi]) == [50, 100, 150, 200, 250, 300, 350]


if __name__ == '__main__':
    unittest.main()