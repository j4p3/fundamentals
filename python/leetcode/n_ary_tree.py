
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

    def __str__(self):
        return str(self.val)


def preorder_traversal_recursive(root_node: 'Node') -> 'List[Int]':
    """Return list of preorder tree traversal recursively
    """
    traversal = []

    def _traverse(node):
        if not node and node.val:
            return
        traversal.append(node.val)
        traversal.extend([_traverse(child) for child in node.children])

    _traverse(root_node)
    return traversal


def preorder_traversal_iterative(root_node: 'Node') -> 'List[Int]':
    """Return list of preorder tree traversal iteratively
    """
    traversal = []
    stack = []
    node = root_node
    stack.append(node)

    while stack:
        node = stack.pop()
        if node:
            traversal.append(node.val)
            stack.extend([child for child in node.children[::-1] if child])

    return traversal


root = Node(1, [Node(i, []) for i in [3, 2, 4]])
root.children[0].children = [Node(i, []) for i in [5, 6]]

# print([n.val for n in root.children])

print(preorder_traversal_recursive(root))
print(preorder_traversal_iterative(root))
