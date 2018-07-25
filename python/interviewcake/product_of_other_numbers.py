import unittest


def get_products_of_all_ints_except_at_index(int_list):
    """Return list of products.

    Naive solution: n^2 nested loop + multiply
    Obnoxious with skipping the append on index but whatever

    Simpler solution:
    Loop once
    Accumulate products as we go
    So, "seed" array with each value. O(n).
    Then "layer" with each successive value - except at its own index.
    Just adds a coefficient. Right?

    Input: [1,2,3,4]
    Intermediate: [1,1,1,1]
    Processing: [1*2*3*4, 1*1*3*4, 1*1*2*4, 1*1*2*3]

    If this "layering" happens n times, we haven't gained anything

    What do products have in common?
    Everything to the left of "4" has "4" in it.
    So 4 should be a common layer across all of those.
    
    Build a base array for each el in list, excepting its own value?

    So intermediate would be:
    [[2,3,4], [1,3,4], ...]
    We already have a prototype, int_list, this should be O(n) depending on pop()

    But then reducing it would be O(n) on each el. No gain.

    Let's store some common products as we go.

    [1, 2, 6, 5, 9]

    We need to accumulate:
    product before i
    product after(?) i

    Can we loop twice?
    Accumulate products before, products after?
    """
    if not int_list or len(int_list) < 2:
        raise ValueError('why test for this')

    # print(int_list)
    
    products = []

    # for i, v in enumerate(int_list):
    #     product = 1
    #     inner_index = 0
    #     while inner_index < len(int_list):
    #         if inner_index != i:
    #             product *= int_list[inner_index]
    #         inner_index += 1
    #     products.append(product)
    # # return products

    # products_before = [1] * len(int_list)
    # products_after = [1] * len(int_list)
    # for i, n in enumerate(int_list):
    #     # [1, 2, 6, 5, 9]
    #     print('adding %d to products_before %d' % (n, i + 1))
    #     products_before[i + 1] *= n
    #     print('adding %d to products_after %d' % (n, i -1))
    #     products_after[i - 1] *= n
    # print(products_before)
    # print(products_after)

    # What's the solution *now*?

    products = []
    before_product = 1
    after_product = 1
    # accumulate value of before product
    for i, n in enumerate(int_list):
        if i != 0:
            before_product *= int_list[i - 1]
        products.append(before_product)

    # accumulate value of after product and add into products
    int_list.reverse()
    for i, n in enumerate(int_list):
        if i != 0:
            after_product *= int_list[i - 1]
        products[len(int_list) - 1 - i] *= after_product

    return products



class Test(unittest.TestCase):

    def test_small_list(self):
        actual = get_products_of_all_ints_except_at_index([1, 2, 3])
        expected = [6, 3, 2]
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = get_products_of_all_ints_except_at_index([8, 2, 4, 3, 1, 5])
        expected = [120, 480, 240, 320, 960, 192]
        self.assertEqual(actual, expected)

    def test_list_has_one_zero(self):
        actual = get_products_of_all_ints_except_at_index([6, 2, 0, 3])
        expected = [0, 0, 36, 0]
        self.assertEqual(actual, expected)

    def test_list_has_two_zeros(self):
        actual = get_products_of_all_ints_except_at_index([4, 0, 9, 1, 0])
        expected = [0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)

    def test_one_negative_number(self):
        actual = get_products_of_all_ints_except_at_index([-3, 8, 4])
        expected = [32, -12, -24]
        self.assertEqual(actual, expected)

    def test_all_negative_numbers(self):
        actual = get_products_of_all_ints_except_at_index([-7, -1, -4, -2])
        expected = [-8, -56, -14, -28]
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([1])


unittest.main(verbosity=2)
# get_products_of_all_ints_except_at_index([1, 2, 6, 5, 9])
