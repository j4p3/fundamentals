import unittest


# def max_duffel_bag_value(cake_tuples, weight_capacity):
#     """The knapsack problem!

#     Strategies:
#     * build every possibility and take max value
#         problem: path-dependent, not the efficient solution
#     * fill with max value cakes (or max value per weight)
#     * build max value ... hash? list? list of lists?
#     * how to dictate swapping out? take max value of remainder?
#     * build max value for n up to capacity
#     * take max value up until each pivot point
#     * but we need to do this remainder trick for each value, for each cake
#     """
#     max_value = [0] * (weight_capacity + 1)
#     for cake in cake_tuples:
#         if cake[0] == 0:
#             # avoid divide by zero
#             if cake[1]:
#                 return float('inf')
#             else:
#                 continue
#         print('analyzing cake %s' % str(cake))
#         for weight in range(cake[0], len(max_value)):
#             base_value = (weight // cake[0]) * cake[1]
#             remainder_value = max_value[weight % cake[0]]
#             print('##%d\n\tbase: %d\n\tremainder: %d\n\tcurrent: %d' % (
#                 weight,
#                 base_value,
#                 remainder_value,
#                 max_value[weight]
#                 ))
#             if base_value + remainder_value > max_value[weight]:
#                 max_value[weight] = base_value + remainder_value

#     # print(max_value)
#     return max_value[weight_capacity]

def max_duffel_bag_value(cakes, capacity):
    if capacity == 0:
        return 0

    haul = [0] * (capacity + 1)

    # @todo: handle divisible capacities, discard less value-dense

    for (weight, value) in cakes:
        if value == 0:
            pass
        elif weight == 0:
            return float('inf')

        if weight < capacity:
            haul[weight] = value

    for i in range(capacity + 1):
        for (weight, value) in cakes:
            if i - weight > 0 and haul[i - weight] + value > haul[i]:
                haul[i] =  haul[i - weight] + value
    
    return haul[-1]

# Tests
class Test(unittest.TestCase):

    def test_one_cake(self):
        actual = max_duffel_bag_value([(2, 1)], 9)
        expected = 4
        self.assertEqual(actual, expected)

    def test_two_cakes(self):
        actual = max_duffel_bag_value([(4, 4), (5, 5)], 9)
        expected = 9
        self.assertEqual(actual, expected)

    def test_only_take_less_valuable_cake(self):
        actual = max_duffel_bag_value([(4, 4), (5, 5)], 12)
        expected = 12
        self.assertEqual(actual, expected)

    def test_lots_of_cakes(self):
        actual = max_duffel_bag_value([(2, 3), (3, 6), (5, 1), (6, 1), (7, 1), (8, 1)], 7)
        expected = 12
        self.assertEqual(actual, expected)

    def test_value_to_weight_ratio_is_not_optimal(self):
        actual = max_duffel_bag_value([(51, 52), (50, 50)], 100)
        expected = 100
        self.assertEqual(actual, expected)

    def test_zero_capacity(self):
        actual = max_duffel_bag_value([(1, 2)], 0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_cake_with_zero_value_and_weight(self):
        actual = max_duffel_bag_value([(0, 0), (2, 1)], 7)
        expected = 3
        self.assertEqual(actual, expected)

    def test_cake_with_non_zero_value_and_zero_weight(self):
        actual = max_duffel_bag_value([(0, 5)], 5)
        expected = float('inf')
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
# print(max_duffel_bag_value([(0, 0), (2, 1)], 7))