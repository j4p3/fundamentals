import unittest


def get_max_profit(stock_prices):
    """
    Find biggest in-order diff.
    What happens with e.g. 5 5 1 5 5 10 5 5 0 5 5 ?
    Biggest trade is 9. Can't use the trailing 0.
    Need some kind of lookback given new highest, right?
    Why lookback? Why not just keep lowest?
    5 5 2 5 5 5 1 10 5 5 
    First 2-5 trade is best. Then we get new low marker. Can't use it.
    However, need to track that new/equal low for potential new diffs
    Tracking a low marker is effectively a backwards looking solution
    """
    low_marker = 0
    best_trade = stock_prices[1] - stock_prices[0]

    if not len(stock_prices) > 1:
        raise ValueError('why would you even test for this')

    for i in range(1, len(stock_prices)):
        # keep best trade so far
        # skip first value, since we've already used it.
        diff = stock_prices[i] - stock_prices[low_marker]
        if diff > best_trade:
            best_trade = diff

        if stock_prices[i] < stock_prices[low_marker]:
            # track new low in case a better diff comes along
            low_marker = i

    return best_trade


class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_one_price_raises_error(self):
        with self.assertRaises(Exception):
            get_max_profit([1])

    def test_empty_list_raises_error(self):
        with self.assertRaises(Exception):
            get_max_profit([])

unittest.main(verbosity=2)
