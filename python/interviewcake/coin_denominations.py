import unittest
import collections


def change_possibilities_hmmm(amount, denominations):
    """Find the number of combinations of coins to make amount

    Strategy: skip space of [amount] and just work per coin - won't work
    ignores lower possibilities
    """
    possibilities = 0

    for denomination in denominations:
        # case denom = 1
        # not poss += 4
        # case denom = 2, amt = 5, no 1: amt // 2  = 2, but answer is 0
        possibilities += amount // denomination


def change_possibilities(amount, denominations):
    """Find the number of combinations of coins to make amount

    Strategy: increment possibilities per coin across space of [amount]
    Refer back to possibility space for remainder possibilities

    Can't make change for nondivisible amount, like 49/5 -
    Solution is only valid if pennies are present
    """
    possibilities = [0] * (amount + 1)
    possibilities[0] = 1

    for denom in denominations:
        print('outer: building denom %d' % denom)

        for i in range(denom, len(possibilities)):
            # prior possibilites exist -> increment?
            #   by number of additional substitution possibilities
            p = possibilities[i - denom]
            print('incrementing %d by %d' % (i, p or 1))
            possibilities[i] += p or 1

    # print(possibilities)

    return possibilities[amount]


def change_possibilities_scratch(amount, denominations):
    """Find the number of combinations of coins to make amount

    Strategies:
    * get as close as possible with one denom
        then solve remainder with other denoms
    * begin with smallest denoms, find number of combinations to create
        larger denoms, treat larger denoms as blocks worth n possibilities
    * dynamic programming problem:
        problem of possibilities for amount is same as problem of possibilities
        for denominations[0], denominations[1], etc
        denominations[-1] has one possibility: itself
        therefore:
            work upwards from smallest denomination
            build combinations for larger denominations by the set of smaller
                denoms that it is divisible by
    """
    denominations

    possibilities_for_coin = collections.defaultdict(int)

    possibilities_for_coin[denominations[0]] = 1

    # create possibility count for denominations above first
    for denom in denominations[1:]:
        divisible_denoms = filter(lambda d: d % denom == 0, denominations)
        # here's the dynamic programming problem:
        if denom not in possibilities_for_coin:
            # problem here: possibilities_for_coin would need to be passed
            # or inner function written to avoid redoing everything
            # could also wrap in class
            possibilities_for_coin[denom] = change_possibilities(
                denom,
                [d for d in divisible_denoms])
            # missing the part where we actually solve change_possibilities for #2
            # .. no, that's below

    # at this point we have possibilities for all denoms
    # now find combination using fewest coins
    # aggregate their possibilities?
    # is it possible to 'miss' possibilities?
    #   e.g. using largest coins works but skips smaller?
    #   28 with (7, 2) - we would get 1 poss, 4x7 coins
    #   but we could also use 14x2 coins
    #   is there something clever and mathy to be done?

    combination_count = collections.defaultdict(int)
    amount_left = amount

    for denom in reversed(denominations):
        if denom < amount_left:
            combination_count[denom] = amount_left // denom

    return combination_count

    # something clever and mathy that could be done: a multiplication table
    # just take each int between 0 and amount, and increment combination count?
    # combination count increment would increase at each multiple
    # so for 2: [0, 0, 1, 0, 1, ..]
    # but if 1 had already been done:
    # [0, 1, 2, 3, 4, 5, ...]
    # [0, 1, 1, 1, 1, 1, ...]
    # [0, 1, 2, 2, 3, 3, ...]
    # layer on subsequent multiples

# Tests
class Test(unittest.TestCase):

    def test_sample_input(self):
        actual = change_possibilities(4, (1, 2, 3))
        expected = 4
        self.assertEqual(actual, expected)

    def test_one_way_to_make_zero_cents(self):
        actual = change_possibilities(0, (1, 2))
        expected = 1
        self.assertEqual(actual, expected)

    def test_no_ways_if_no_coins(self):
        actual = change_possibilities(1, ())
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_coin_value(self):
        actual = change_possibilities(5, (25, 50))
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_target_amount(self):
        actual = change_possibilities(50, (5, 10))
        expected = 6
        self.assertEqual(actual, expected)

    def test_change_for_one_dollar(self):
        actual = change_possibilities(100, (1, 5, 10, 25, 50))
        expected = 292
        self.assertEqual(actual, expected)


# unittest.main(verbosity=2)
# print(change_possibilities(4, (1, 2, 3)))
print(change_possibilities(29, (5, 10)))
# print(change_possibilities(100, (1, 5, 10, 25, 50)))
