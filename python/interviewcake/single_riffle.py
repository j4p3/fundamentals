import unittest


def is_single_riffle(half1, half2, shuffled_deck):
    # Check if the shuffled deck is a single riffle of the halves
    # In the case that the deck is a 'single riffle':
    #   cards will retain order from half1 & half2
    #   algorithm:
    #       iterate through shuffled_deck
    #       top card of shuffled_deck must be top card of half1 or half2
    #       pop card from half1/half2, next
    # 
    # can probably be improved by making a deque instead, since pop(0) is slow
    for card in shuffled_deck:
        if len(half1) and card == half1[0]:
            half1.pop(0)
        elif len(half2) and card == half2[0]:
            half2.pop(0)
        else:
            return False
    return True


# Tests
class Test(unittest.TestCase):

    def test_both_halves_are_the_same_length(self):
        result = is_single_riffle([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_halves_are_different_lengths(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_half_is_empty(self):
        result = is_single_riffle([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_shuffled_deck_is_missing_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_shuffled_deck_has_extra_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)


unittest.main(verbosity=2)
