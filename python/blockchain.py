import unittest


def longest_chain(chain):
    # Places for improvement:
    # how to avoid stepping through entire chain n(leaves) times?
    # how to walk through list once, assigning values to one/multiple chains
    # as necessary, then compare chains at end?

    leaves = []
    chains = []
    longest = []

    # get leaves
    # O(n)
    for i in range(len(chain)):
        if (i not in chain):
            leaves.append(i)

    # follow leaves to root to record chains
    # O(n)
    for leaf in leaves:
        chains.append([])
        block_address = leaf
        while (block_address != -1):
            chains[-1].append(block_address)
            block_address = chain[block_address]

    # compare chain lengths
    # O(n)
    for chain in chains:
        if (len(chain) > len(longest)):
            longest = chain

    longest.reverse()
    print(longest)
    return longest


class Test(unittest.TestCase):
    def test_chain(self):
        chain = [6,7,1,2,2,1,5,-1,0,6]

        result = longest_chain(chain)
        self.assertEqual(len(result), 6)


unittest.main()
