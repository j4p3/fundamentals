import unittest


def fib(n):
    """Return position n of a 0 index, 0 start fibonacci series

    Strategy: recurse.
    Build result table for large numbers.
    """

    if n < 0:
        raise ValueError('give me a break')

    results = {}

    def _fib(i):
        if i <= 1:
            return i
        elif i in results:
            return results[i]

        result = fib(i - 1) + fib(i - 2)
        results[i] = result
        return result

    return _fib(n)


def fib_bottom_up(n):
    if n < 0:
        raise ValueError('give me a break')
    elif n <= 1:
        return n

    result = 0
    past_n = 0
    last_n = 1

    for _ in range(n - 1):  # 0 indexed series
        result = past_n + last_n
        past_n = last_n
        last_n = result

    return result


# Tests
class Test(unittest.TestCase):

    def test_zeroth_fibonacci(self):
        actual = fib(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_first_fibonacci(self):
        actual = fib(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_second_fibonacci(self):
        actual = fib(2)
        expected = 1
        self.assertEqual(actual, expected)

    def test_third_fibonacci(self):
        actual = fib(3)
        expected = 2
        self.assertEqual(actual, expected)

    def test_fifth_fibonacci(self):
        actual = fib(5)
        expected = 5
        self.assertEqual(actual, expected)

    def test_tenth_fibonacci(self):
        actual = fib(10)
        expected = 55
        self.assertEqual(actual, expected)

    def test_negative_fibonacci(self):
        with self.assertRaises(Exception):
            fib(-1)


# unittest.main(verbosity=2)
print(fib(24))
print(fib_bottom_up(24))
