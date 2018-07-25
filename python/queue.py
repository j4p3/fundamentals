import unittest
import collections


class Queue():
    def __init__(self):
        self._queue = []

    def enqueue(self, value):
        self._queue.insert(0, value)
        return value

    def dequeue(self):
        return self._queue.pop()


class QueueFromDeque():
    def __init__(self):
        self._queue = collections.deque()

    def enqueue(self, value):
        self._queue.append(value)
        return value

    def dequeue(self):
        return self._queue.popleft()


class Test(unittest.TestCase):
    def test_queue(self):
        q = Queue()
        for i in range(150000):
            q.enqueue(i)
        self.assertEqual(q.dequeue(), 0)
        q.enqueue(99)
        q.enqueue(101)
        self.assertEqual(q.dequeue(), 1)

    def test_deque_queue(self):
        q = QueueFromDeque()
        for i in range(150000):
            q.enqueue(i)
        self.assertEqual(q.dequeue(), 0)
        q.enqueue(99)
        q.enqueue(101)
        self.assertEqual(q.dequeue(), 1)


unittest.main(verbosity=2)
