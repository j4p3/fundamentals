import pdb
import unittest


class Node(object):
    def __init__(self, key=None):
        self.key = key
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.key)


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail

    def __str__(self):
        nodes = []
        node = self.head
        while node.next != self.tail:
            node = node.next
            nodes.append(str(node))
        # pdb.set_trace()
        return str(nodes)

    def insert(self, key):
        # add to head
        print("inserting key %s" % key)
        new_node = Node(key)
        new_node.next = self.head.next
        self.head.next = new_node
        return new_node

    def append(self, key):
        # add to tail
        new_node = Node(key)
        ref_node = self.head
        while ref_node.next != self.tail:
            ref_node = ref_node.next
        new_node.next = ref_node.next
        ref_node.next = new_node
        return new_node

    def search(self, key):
        node = self.head.next
        while node.key != key and node != self.head:
            node = node.next

        if node == node.head:
            return -1

        return node

    def remove(self, node):
        # circular references?
        ref_node = node.next
        while ref_node.next != node:
            ref_node = ref_node.next

        ref_node.next = node.next


class DoublyLinkedList:
    def __init__(self):
        self.head = None


class Test(unittest.TestCase):

    def test_linked_list_insert(self):
        ll = LinkedList()
        for i in range(15):
            ll.insert(i)
        self.assertEqual('14', str(ll.head.next))

    def test_linked_list_append(self):
        ll = LinkedList()
        for i in range(15):
            ll.append(i)
        self.assertEqual('0', str(ll.head.next))


unittest.main(verbosity=2)

# ll = LinkedList()
# for i in range(15):
#     ll.append(i)
# # ll.append(99)
# print(ll)
