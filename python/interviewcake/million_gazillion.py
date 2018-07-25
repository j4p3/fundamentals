import random
import string

# Objective: reduce space of visited

visited = {'foo.com', 'bar.com', 'baz.com'}  # etc

# idea: hash table for URLs
# probably faster access, anyway
# we'll use built-in hash


class Node:
    """Hashtable doubly linked list value"""

    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)


class LinkedList:
    """Linked List"""

    def __init__(self):
        self.sentinel = Node(None)

    def __str__(self):
        node = self.sentinel
        output = []
        while node.next:
            node = node.next
            output.append(node)
        return ', '.join([str(x) for x in output])

    def insert(self, value):
        ref_node = self.sentinel.next
        new_node = Node(value)
        new_node.next = ref_node
        self.sentinel.next = new_node
        return new_node


class HashTable:
    """Hashtable"""

    def __init__(self):
        self._maxsize = 100
        self._slots = [None] * self._maxsize

    def __str__(self):
        output = ''
        for slot in self._slots:
            output += '%s\n' % slot
        return output

    def insert(self, value):
        hashed = hash(value) % self._maxsize
        if self._slots[hashed]:
            print('inserting %s at occupied slot %s' % (value, hashed))
            return self._slots[hashed].insert(value)
        else:
            print('inserting %s in new slot %s' % (value, hashed))
            self._slots[hashed] = LinkedList()
            return self._slots[hashed].insert(value)


reduced_fat_visited = HashTable()
for site in visited:
    reduced_fat_visited.insert(site)
for i in range(500):
    reduced_fat_visited.insert(''.join(random.choices(string.ascii_lowercase, k=10))+'.com')
print(reduced_fat_visited)
