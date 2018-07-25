import unittest
import math


def reverse(list_of_chars):
    for i in range(math.floor(len(list_of_chars) / 2)):
        list_of_chars[i], list_of_chars[-(i + 1)] = \
            list_of_chars[-(i + 1)], list_of_chars[i]


def reverse_words(message):
    """
    reverse full message (O(n))
    walk through until breaks
    reverse preceding word(O(n))
    """
    reverse(message)

    word = []
    for i, c in enumerate(message):
        if c is ' ':
            for wi, wc in enumerate(word):
                message[i - (wi + 1)] = wc
            word.clear()
        else:
            word.append(c)
    for wi, wc in enumerate(word):
                message[i - (wi)] = wc


class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)
