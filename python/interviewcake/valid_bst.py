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

    def traverse(self):
        nodes = []
        nodes.append(self.is_valid(self.left) if self.left else nodes)
        nodes.append(self)
        nodes.append(self.is_valid(self.right) if self.right else nodes)

    def is_valid(self):
        traversal = self.traverse()
        for i in traversal.iterkeys():
            if traversal[i] > traversal[i + 1]:
                return False
        return True
