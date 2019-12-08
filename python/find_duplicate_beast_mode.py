import unittest


def find_duplicate(int_list):
    """Find a number that appears more than once ... in O(n) time
     .. and O(1) space

     Easy trick: since each value can be thought of as "pointer" to another
     position (not index but ordinal position) on the list,

     We can traverse list as linked list/graph.
     Guaranteed to end in loop.
     Duplicate guaranteed to be in loop.

     How to find loop without eating space?
     Can't keep stack/dict of visited indeces

     Could just iterate n times until we're sure we're in it, then create loop
    """

    # 1. find index of any element inside loop
    # print('testing:')
    # print(int_list)
    ref_idx = len(int_list) - 1

    for i in range(len(int_list)):
        ref_idx = int_list[ref_idx - 1]

    # print('ref_idx: %d' % ref_idx)

    # 2. measure loop length
    # print('measuring cycle length')
    cycle_head = ref_idx
    ref_idx = int_list[ref_idx - 1]
    cycle_length = 1
    while ref_idx != cycle_head:
        cycle_length += 1
        ref_idx = int_list[ref_idx - 1]

    # print('cycle length: %d' % cycle_length)

    # 3. iterate until start pointer same as end pointer

    start_pos = end_pos = len(int_list)
    for i in range(cycle_length):  # initialize end_pos n steps ahead
        end_pos = int_list[end_pos - 1]

    while start_pos != end_pos:
        start_pos = int_list[start_pos - 1]
        end_pos = int_list[end_pos - 1]

    return start_pos


# Tests
class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_duplicate([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_duplicate([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_duplicate([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_duplicate([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
# print(find_duplicate([4, 1, 4, 8, 3, 2, 7, 6, 5]))
# print(find_duplicate([1, 2, 5, 5, 5, 5]))
# print(find_duplicate([1, 2, 3, 2]))
