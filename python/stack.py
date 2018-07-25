import unittest


class Stack():
    def __init__(self):
        self._stack = []

    def push(self, value):
        self._stack.append(value)
        return value

    def pop(self):
        return self._stack.pop()


class Test(unittest.TestCase):
    def test_stack(self):
        stack = Stack()
        for i in range(15):
            stack.push(i)
        self.assertEqual(stack.pop(), 14)
        stack.push(5)
        stack.push(55)
        self.assertEqual(stack.pop(), 55)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.pop(), 13)


unittest.main(verbosity=2)
