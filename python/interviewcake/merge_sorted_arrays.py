import unittest


def merge_lists(a_list, b_list):
    new_list = []
    a_idx = b_idx = 0

    while a_idx < len(a_list) or b_idx < len(b_list):
        if (b_idx >= len(b_list) or
                a_idx < len(a_list) and
                a_list[a_idx] < b_list[b_idx]):
            new_list.append(a_list[a_idx])
            a_idx += 1
        else:
            new_list.append(b_list[b_idx])
            b_idx += 1
    return new_list


# Tests
class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
# merge_lists([2, 4, 6], [1, 3, 7])
