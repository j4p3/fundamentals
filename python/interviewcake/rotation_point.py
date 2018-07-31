import unittest
import math

words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]


def find_rotation_point(words):
    """
    The idea is to start at the middle and jump to "a"
    or rather, to the point where "not a" becomes "a"
    or rather, to i where [i - 1] < [i] == False

    Difficulty is that condition isn't as simple as a < b left, a > b right.
    i - 1 will always be < i except at one point.
    We're searching for minimum, really, where minimum is an alphabetical value

    Bit tricky with off-by-ones since we're looking to narrow down to a pair,
    then take the greater index. Might as well just grab upper bound.
    """
    if words[0] < words[-1]:
        # unshifted case - take first word.
        return 0

    lower_bound = 0
    upper_bound = len(words) - 1

    # iterate until narrowed down to a pair, return greater of pair
    while lower_bound < upper_bound - 1:
        # find midpoint
        delimiter = math.floor(lower_bound + (upper_bound - lower_bound) / 2)

        # raise floor if undershot, drop ceiling if overshot
        if words[delimiter] < words[lower_bound]:
            upper_bound = delimiter
        else:
            lower_bound = delimiter

    return upper_bound


class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    def test_already_ordered(self):
        actual = find_rotation_point(['a', 'bncd', 'efgh'])
        expected = 0
        self.assertEqual(actual, expected)

    def test_second_word(self):
        actual = find_rotation_point(['zdfa', 'a', 'bncd', 'efgh'])
        expected = 1
        self.assertEqual(actual, expected)

    # Are we missing any edge cases?


unittest.main(verbosity=2)