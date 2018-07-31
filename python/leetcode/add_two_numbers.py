import unittest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode

    Strategies:
    * munge together llists into strings, into ints, add, and space back out into llists
        problem: O(n)
    * is there a better than O(n) solution here? We need to at least look at every node, right?
    """

    str1 = ''
    str2 = ''

    while l1:
        str1 += str(l1.val)
        l1 = l1.next
    while l2:
        str2 += str(l2.val)
        l2 = l2.next

    int1 = int(''.join([i for i in reversed(str1)]))
    int2 = int(''.join([i for i in reversed(str2)]))

    result = [i for i in reversed(str(int1 + int2))]
    root = node = ListNode(int(result[0]))

    for i in result[1:]:
        node.next = ListNode(int(i))
        node = node.next

    return root


class Test(unittest.TestCase):
    def test_example_input(self):
        # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
        # Output: 7 -> 0 -> 8
        i1 = [2, 4, 3]
        i2 = [5, 6, 4]
        expected_result = [7, 0, 8]
        root1 = node1 = ListNode(i1[0])
        root2 = node2 = ListNode(i2[0])
        for i in i1[1:]:
            node1.next = ListNode(i)
            node1 = node1.next
        for i in i2[1:]:
            node2.next = ListNode(i)
            node2 = node2.next
        result = add_two_numbers(root1, root2)

        result_index = 0
        while result:
            print('%d - %d' % (result.val, expected_result[result_index]))
            self.assertEqual(result.val, expected_result[result_index])
            result_index += 1
            result = result.next

unittest.main()
