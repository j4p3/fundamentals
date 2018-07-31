import unittest
# import random


class Node:
    """Base tree node"""

    def __init__(self, value):
        self.value = value
        self.p = None
        self.left = None
        self.right = None
        self.color = None

    def __str__(self):
        return '<%d>' % self.value

    def height(self):
        return max(
            self.left.height() + 1 if self.left else 1,
            self.right.height() + 1 if self.right else 1,
        )

    def minimum(self):
        if not self.left:
            return self.value
        return self.left.minimum()

    def maximum(self):
        if not self.right:
            return self.value
        return self.right.maximum()

    def successor(self):
        if self.right:
            return self.right.minimum
        reference_node = self
        parent_node = self.p
        while parent_node and reference_node is parent_node.right:
            parent_node = parent_node.p
            reference_node = parent_node
        return parent_node

    def predecessor(self):
        if self.left:
            return self.left.maximum
        reference_node = self
        parent_node = self.p
        while parent_node and reference_node is parent_node.left:
            parent_node = parent_node.p
            reference_node = parent_node
        return parent_node


class BinaryTree:
    """Binary tree"""

    def __init__(self, value=None):
        self.root = Node(value)

    def height(self):
        return self.root.height()

    def minimum(self):
        return self.root.minimum()

    def maximum(self):
        return self.root.maximum()

    def insert(self, value, node=None):
        # check for first insertion
        if not self.root.value:
            self.root.value = value
            return self.root

        # check for blank insertion
        node = self.root if not node else node

        if value < node.value:
            if not node.left:
                node.left = Node(value)
                node.left.p = node
                return node.left
            return self.insert(value, node.left)

        if not node.right:
            node.right = Node(value)
            node.right.p = node
            return node.right
        return self.insert(value, node.right)

    def search(self, value):
        pass

    def traverse_in_order(self):
        nodes = []
        def _traverse(node):
            if not node:
                return
            _traverse(node.left)
            nodes.append(node)
            _traverse(node.right)
        _traverse(self.root)
        return nodes


COLORS = {
    'RED': 1,
    'BLACK': 2,
}


class RedBlackTree(BinaryTree):
    """Red-Black tree"""

    def __init__(self):
        self.root = None

    def insert(self, value, node=None):
        self.root = self._insert(value, self.root)
        self.root.color = COLORS['RED']
        return self.root

    def _insert(self, value, node):
        insertion_root = node

        if node is None:
            new_node = Node(value)
            new_node.color = COLORS['RED']
            return new_node

        if value <= node.value:
            node.left = self._insert(value, node.left)
        else:
            node.right = self._insert(value, node.right)

        if node.right and node.right.color == COLORS['RED'] and \
           node.left and node.left.color == COLORS['BLACK']:
            insertion_root = self._left_rotate(node)

        if node.left and node.left.color == COLORS['RED'] and \
           node.left.left and node.left.left.color == COLORS['RED']:
            insertion_root = self._right_rotate(node)

        if node.right and node.right.color == COLORS['RED'] and \
           node.left and node.left.color == COLORS['RED']:
            node.right.color = COLORS['BLACK']
            node.left.color = COLORS['BLACK']

        return insertion_root

    def _left_rotate(self, node):
        """
            x
           / \
          a   y
             / \
            b   c
        """
        y = node.right
        if y:
            node.right = y.left
            y.left = node
            y.color = node.color
            node.color = COLORS['RED']
        return y

    def _right_rotate(self, node):
        """
            y
           / \
          x   c
         / \
        a   b
        """
        x = node.left
        if x:
            node.left = x.right
            x.right = node
            x.color = node.color
            node.color = COLORS['RED']
        return x

    def successor(self, node):
        pass

        # fixup:
        # right red, left black
        # insertion_root = lrotate

        # left red, left-left red
        # insertion_root = rrotate

        # left red, right red
        # flip colors of both


class Test(unittest.TestCase):
    TEST_LIST = [36, 11, 42, 24, 31, 12, 11, 32, 1, 27, 6, 39, 4, 12, 18, 13, 39, 21, 26, 1]

    def test_node_height(self):
        n = Node(5)
        n.left = Node(4)
        n.right = Node(6)
        n.right.right = Node(15)
        self.assertEqual(n.height(), 3)

    def test_binary_tree(self):
        t = BinaryTree()
        for r in self.TEST_LIST:
            t.insert(r)

        self.assertEqual(t.height(), 7)
        self.assertEqual(t.minimum(), 1)
        self.assertEqual(t.maximum(), 42)

    def test_red_black_tree(self):
        t = RedBlackTree()
        for r in self.TEST_LIST:
            t.insert(r)

        print(t.height())
        self.assertEqual(t.minimum(), 1)
        self.assertEqual(t.maximum(), 42)


unittest.main(verbosity=2)

# t = RedBlackTree()
# for r in Test.TEST_LIST:
#     t.insert(r)
# print([str(i) for i in t.traverse_in_order()])
# print(t.maximum())
