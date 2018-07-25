import unittest


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def insert(self, val):
        self.next = Node(val)


def can_two_movies_fill_flight(movie_lengths, flight_length):
    """
    Initial thoughts:
    Looking for every possible unique combination of lengths.
    n^2 if we iterate twice
    What's better?
    I want a batch operation against every element in the list. That'd be n
    Hash table.
    Key is valid flight lengths
    But building hash table would still be n^2, yes?

    no! because we'd have pre-made the table. inner loop isn't going to be n, it'll be 1
    """
    # build table
    length_table = {}
    for movie_length in movie_lengths:
        if movie_length in length_table:
            length_table[movie_length].insert(movie_length)
        else:
            length_table[movie_length] = Node(movie_length)

    for movie_length in movie_lengths:
        viable_second_movie = length_table.get(flight_length - movie_length)

        if viable_second_movie:
            if movie_length != viable_second_movie.val:
                return True
            if viable_second_movie.next:
                return True
    return False


class Test(unittest.TestCase):

    def test_short_flight(self):
        result = can_two_movies_fill_flight([2, 4], 1)
        self.assertFalse(result)

    def test_long_flight(self):
        result = can_two_movies_fill_flight([2, 4], 6)
        self.assertTrue(result)

    def test_one_movie_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8], 6)
        self.assertFalse(result)

    def test_two_movies_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8, 3], 6)
        self.assertTrue(result)

    def test_lots_of_possible_pairs(self):
        result = can_two_movies_fill_flight([1, 2, 3, 4, 5, 6], 7)
        self.assertTrue(result)

    def test_only_one_movie(self):
        result = can_two_movies_fill_flight([6], 6)
        self.assertFalse(result)

    def test_no_movies(self):
        result = can_two_movies_fill_flight([], 2)
        self.assertFalse(result)


unittest.main(verbosity=2)
