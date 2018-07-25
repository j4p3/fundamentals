import unittest
from functools import reduce


def highest_product_of_3(list_of_ints):
    """Give the highest possible product of three ints from a list of ints.

    Args:
        list_of_ints (list[int])

    Returns:
        int: highest possible product of three elementsi n list

    Naive/brute force solution:
        triply nested loop

    Ideally we'll just look through list once, grabbing our likeliest candidates

    Take first three, then compare each against our previous best

    Bump minimum each time

    Wait, we just want the three highest numbers.

    Wrong, negative numbers tip the scales ... if we have two of them.
    """

    # Shelving this approach since it only works with positive ints
    # highest_ints = list_of_ints[0:3]

    # for i in list_of_ints[3:]:
    #     if min(highest_ints + [i]) is not i:
    #         highest_ints[highest_ints.index(min(highest_ints))] = i

    # print(highest_ints)
    # return highest_ints[0] * highest_ints[1] * highest_ints[2]

    # negative-positive situation:
    # 1 -10 -10, product = 100
    # now we get a 50.
    # 1 -10 50 doesn't work.
    # 1 3 50 works, though.
    # so we can't just throw things onto the product.
    # we need to remember previous max values per sign

    if len(list_of_ints) < 3:
        raise ValueError('why would you even test for this')

    max_values = []
    max_negatives = []

    for i in list_of_ints:
        # handle new max negative
        if i < 0 and len(max_negatives) <= 1:
            max_negatives.append(i)
        elif i < 0 and \
                len(max_negatives) is 2 and \
                max(max_values + [i]) is not i:
            max_negatives[max_negatives.index(max(max_negatives))] = i

        # handle new max
        if len(max_values) < 3:
            max_values.append(i)
        elif min(max_values + [i]) is not i:
            max_values[max_values.index(min(max_values))] = i

    product = max_values[0] * max_values[1] * max_values[2]

    if len(max_negatives) is 2:
        print('found two negatives')
        print(max_negatives)
        print(max_values)
        return max(max_negatives[0] * max_negatives[1] * max(max_values),
                   product)
    return product


class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)
