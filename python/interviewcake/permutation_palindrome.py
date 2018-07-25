import unittest
from collections import defaultdict


def has_palindrome_permutation(the_string):
    """
    Envisioning an intermediate step that is string permutation list
    How to get all possible permutations? Single pass through string
    Pop current char
    Create new string for each possible choice
    likely n! operation. Can we create permuation without going n!?

    Go from both sides?

    Check if a matching char exists for each char except, potentially, one.

    Iterate once and build hashtable with linkedlist.
    Iterate again to verify length of each slot is even number

    Don't like idea of writing a Node, inserting, etc. Gotta be easier way.
    """
    frequency_count = defaultdict(int)

    # frequency count
    for char in the_string:
        frequency_count[char] += 1

    found_single = False
    for letter in frequency_count:
        if frequency_count[letter] % 2:
            # letter occurs odd number of times
            if found_single:
                # this can only happen once in a palindrome
                return False
            found_single = True

    # if we haven't found enough singletons, it's a palindrome
    return True


class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)
