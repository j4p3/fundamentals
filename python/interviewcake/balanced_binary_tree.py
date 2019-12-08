import unittest


class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


def is_balanced(tree_root):
    """Detect whether given tree is 'superbalanced': depth delta btw
    all leaf nodes no greater than one

    Strat:
    * Traverse the whole tree, store a 'depth' property, push leaves into list
    * Traverse down to leaf node, only ascend/descend to the leaves
    *   this will be equivalent to traversing whole tree
    """
    leaves = []
    tree_root.depth = 0
    nodes_to_traverse = [tree_root]

    while nodes_to_traverse:
        current_node = nodes_to_traverse.pop()
        if current_node.left:
            current_node.left.depth = current_node.depth + 1
            nodes_to_traverse.append(current_node.left)
        if current_node.right:
            current_node.right.depth = current_node.depth + 1
            nodes_to_traverse.append(current_node.right)

        if not current_node.left and not current_node.right:
            leaves.append(current_node)

    diff = max([n.depth for n in leaves]) - min([n.depth for n in leaves])
    return diff <= 1


# Tests
class Test(unittest.TestCase):

    def test_full_tree(self):
        tree = BinaryTreeNode(5)
        left = tree.insert_left(8)
        right = tree.insert_right(6)
        left.insert_left(1)
        left.insert_right(2)
        right.insert_left(3)
        right.insert_right(4)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_both_leaves_at_the_same_depth(self):
        tree = BinaryTreeNode(3)
        left = tree.insert_left(4)
        right = tree.insert_right(2)
        left.insert_left(1)
        right.insert_right(9)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_leaf_heights_differ_by_one(self):
        tree = BinaryTreeNode(6)
        left = tree.insert_left(1)
        right = tree.insert_right(0)
        right.insert_right(7)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_leaf_heights_differ_by_two(self):
        tree = BinaryTreeNode(6)
        left = tree.insert_left(1)
        right = tree.insert_right(0)
        right_right = right.insert_right(7)
        right_right.insert_right(8)
        result = is_balanced(tree)
        self.assertFalse(result)

    def test_three_leaves_total(self):
        tree = BinaryTreeNode(1)
        left = tree.insert_left(5)
        right = tree.insert_right(9)
        right.insert_left(8)
        right.insert_right(5)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_both_subtrees_superbalanced(self):
        tree = BinaryTreeNode(1)
        left = tree.insert_left(5)
        right = tree.insert_right(9)
        right_left = right.insert_left(8)
        right.insert_right(5)
        right_left.insert_left(7)
        result = is_balanced(tree)
        self.assertFalse(result)

    def test_only_one_node(self):
        tree = BinaryTreeNode(1)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_linked_list_tree(self):
        tree = BinaryTreeNode(1)
        right = tree.insert_right(2)
        right_right = right.insert_right(3)
        right_right.insert_right(4)
        result = is_balanced(tree)
        self.assertTrue(result)


unittest.main(verbosity=2)
