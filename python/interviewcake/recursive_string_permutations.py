import unittest


def get_permutations(string):
    """Recursive permeutation generator

    Solution is permeutation of permeutations
    What is base case? single letter (or double letter)
    Return single letter.
    Given double letter, return both orders.
    Given two double letters? Or two pairs of double letters? How to combine?

    Just go left-right or right-left and drop the next letter in each slot.

    Base case is a single letter
    """

    # base case: return base set of one char
    if len(string) <= 1:
        return set([string])

    # normal case: combine last letter with results of recursion
    permutations = set()

    # pop a letter
    # combine letter with all subpermutations
    # return new combined permutations
    perms_of_trimmed_string = get_permutations(string[:-1])

    for perm in perms_of_trimmed_string:
        for i in range(len(string)):
            new_perm = perm[:i] + string[-1] + perm[i:]
            permutations.add(new_perm)

    return permutations


def get_permutations_example(string):
    # Base case
    if len(string) <= 1:
        return set([string])

    all_chars_except_last = string[:-1]
    last_char = string[-1]

    # Recursive call: get all possible permutations for all chars except last
    permutations_of_all_chars_except_last = get_permutations(all_chars_except_last)

    # Put the last char in all possible positions for each of
    # the above permutations
    permutations = set()
    for permutation_of_all_chars_except_last in permutations_of_all_chars_except_last:
        for position in range(len(all_chars_except_last) + 1):
            permutation = (
                permutation_of_all_chars_except_last[:position]
                + last_char
                + permutation_of_all_chars_except_last[position:]
            )
            permutations.add(permutation)

    return permutations


# Tests
class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
# print(get_permutations('cats'))
# print(get_permutations_orig('cats'))
