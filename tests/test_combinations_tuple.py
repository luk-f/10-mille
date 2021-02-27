import unittest
from combinations_tuple import CombinationsTuple
from combination import *

class TestCombinationsTuple(unittest.TestCase):

    def test_init(self):
        my_ct = CombinationsTuple()
        assert len(my_ct) == 0, "doit être vide"
        my_ct = CombinationsTuple([SUITE_1, JUST_1])
        assert len(my_ct) == 2, "doit contenir 2 combinations"

    def test_score(self):
        my_ct = CombinationsTuple()
        assert my_ct.total_score() == 0, "score doit être 0"
        my_ct = CombinationsTuple([SUITE_1, JUST_1])
        assert my_ct.total_score() == 1100, "score doit être 1100"

    def test_add(self):
        my_ct = CombinationsTuple([SUITE_1, JUST_1]) + CombinationsTuple([SUITE_1, JUST_1])
        assert len(my_ct) == 4, "doit contenir 4 combinations"
        assert my_ct.total_score() == 2200, "score doit être 2200"

    def test_set_able(self):
        """
        Teste si CombinationsTuple est hashable est peut être inseré dans un set()
        """
        my_ct = CombinationsTuple([SUITE_1, JUST_1])
        my_set = set()
        my_set.add(my_ct)
        print(my_set)
        print()
        my_ct = CombinationsTuple([JUST_1, SUITE_1])
        my_set.add(my_ct)
        print(my_set, end="\n\n")
        for ct_tmp in my_set:
            print(ct_tmp)
            print(ct_tmp.__hash__())


if __name__ == '__main__':
    unittest.main()

    # my_combituple = CombinationsTuple([SUITE_2, JUST_1])
    # print(my_combituple)
    # print(my_combituple.total_score())
    # print(my_combituple.number_of_dices())
    # print(my_combituple.combination_of_dices())