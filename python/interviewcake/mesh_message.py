import unittest
from collections import deque


def bfs_get_path(graph: 'Dict', node: 'Node', target: 'Node') -> 'List[Node]':
    """Find a path from node to destination

    * BFS is always going to involve pushing nodes into a queue
    * then dequeuing them and doing something to them
    *   i.e. check for target or enqueue neighbors/children

    Current algo is correct, it's just that graph is cyclic
    """
    path = []
    queue = deque()
    queue.append(node)
    path_map = {node: None}

    if target not in graph:
        raise ValueError('come on')

    while len(queue) > 0:
        current_node = queue.popleft()

        if current_node == target:
            queue.clear()
            break
        else:
            for neighbor in graph[current_node]:
                if neighbor not in path_map:
                    queue.append(neighbor)
                    path_map[neighbor] = current_node

    # case: no route to target
    if current_node != target:
        return None

    while current_node:
        path.append(current_node)
        current_node = path_map[current_node]

    path.reverse()
    return path


class Test(unittest.TestCase):

    def setUp(self):
        self.graph = {
            'a': ['b', 'c', 'd'],
            'b': ['a', 'd'],
            'c': ['a', 'e'],
            'd': ['a', 'b'],
            'e': ['c'],
            'f': ['g'],
            'g': ['f'],
        }

    def test_two_hop_path_1(self):
        actual = bfs_get_path(self.graph, 'a', 'e')
        expected = ['a', 'c', 'e']
        self.assertEqual(actual, expected)

    def test_two_hop_path_2(self):
        actual = bfs_get_path(self.graph, 'd', 'c')
        expected = ['d', 'a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_1(self):
        actual = bfs_get_path(self.graph, 'a', 'c')
        expected = ['a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_2(self):
        actual = bfs_get_path(self.graph, 'f', 'g')
        expected = ['f', 'g']
        self.assertEqual(actual, expected)

    def test_one_hop_path_3(self):
        actual = bfs_get_path(self.graph, 'g', 'f')
        expected = ['g', 'f']
        self.assertEqual(actual, expected)

    def test_zero_hop_path(self):
        actual = bfs_get_path(self.graph, 'a', 'a')
        expected = ['a']
        self.assertEqual(actual, expected)

    def test_no_path(self):
        actual = bfs_get_path(self.graph, 'a', 'f')
        expected = None
        self.assertEqual(actual, expected)

    def test_start_node_not_present(self):
        with self.assertRaises(Exception):
            bfs_get_path(self.graph, 'h', 'a')

    def test_end_node_not_present(self):
        with self.assertRaises(Exception):
            bfs_get_path(self.graph, 'a', 'h')


unittest.main(verbosity=2)
