import unittest
import math


def find_repeat(the_list):
    """Return an int occurring twice in the list

    Strategy: walk through list and grab the first duplicate?
    Push items into set and check set for existing dupes?

    Problem: instructions are to optimize for space.
    Solve first, optimize later.

    Optimization: initial strat has O(n) additional space.
    Possible to make do with less? Sort list and walk through?

    Secondary optimization: problem requests not destroying input
    Hm. Any nlogn solution is going to sort it?
    Solution: treat list indeces as presorted list
    """
    # Solution 1: non space optimized
    # seen = {the_list[0]}

    # for el in the_list[1:]:
    #     if el in seen:
    #         return el
    #     seen.add(el)
    # return 0

    # Solution 2: space optimized, destructive in-place operation
    # sort list in place
    # alternatively, could implement quicksort
    # the_list.sort()

    # for i, el in enumerate(the_list):
    #     if the_list[i+1] == el:
    #         return el
    # return 0

    # Solution 3: space optimized & non-destructive
    # problem also requests not destroying list. hmm
    # floor not set to 0 only because we're only looking at indeces within
    #   known range of list values, and we're using indeces as stand-ins
    #   for list values here to find outlier
    floor = 1
    ceiling = len(the_list) - 1

    while floor < ceiling:
        midpoint = floor + math.floor((ceiling - floor) / 2)
        lower_range_floor, lower_range_ceiling = floor, midpoint
        upper_range_floor, upper_range_ceiling = midpoint + 1, ceiling
        lower_range_size = lower_range_ceiling - lower_range_floor + 1

        slottable_into_lower_range = 0
        for el in the_list:
            if el >= lower_range_floor and el <= lower_range_ceiling:
                slottable_into_lower_range += 1

        if slottable_into_lower_range > lower_range_size:
            floor = lower_range_floor
            ceiling = lower_range_ceiling
        else:
            floor = upper_range_floor
            ceiling = upper_range_ceiling

    return floor


class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
