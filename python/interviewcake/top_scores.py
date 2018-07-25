import unittest


def sort_scores(unsorted_scores, highest_possible_score):
    # build table of all possible scores
    score_table = [0 for n in range(highest_possible_score + 1)]
    sorted_scores = []

    # populate table with actual scores
    for score in unsorted_scores:
        score_table[score] += 1

    # return scores
    # surely there is a little one liner list comprehension way to do this
    for score, quantity in enumerate(score_table):
        if quantity:
            sorted_scores.extend([score] * quantity)
    sorted_scores.reverse()
    return sorted_scores


class Test(unittest.TestCase):

    def test_no_scores(self):
        actual = sort_scores([], 100)
        expected = []
        self.assertEqual(actual, expected)

    def test_one_score(self):
        actual = sort_scores([55], 100)
        expected = [55]
        self.assertEqual(actual, expected)

    def test_two_scores(self):
        actual = sort_scores([30, 60], 100)
        expected = [60, 30]
        self.assertEqual(actual, expected)

    def test_many_scores(self):
        actual = sort_scores([37, 89, 41, 65, 91, 53], 100)
        expected = [91, 89, 65, 53, 41, 37]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
