# You've got a table full of marbles.
# You can remove a marble if it shares its x coordinates
# or y coordinates with another marble.
#
# Write a function that will tell:
# given the positions of the marbles -
# how many marbles will be left over
# after all possible marbles have been removed


class AxisGraph:
    def __init__(self, marbles):
        # print(marbles)
        self.x = {}
        self.y = {}

        for marble in marbles:
            # print('adding marble %s' % str(marble))
            if marble[0] not in self.x:
                self.x[marble[0]] = [marble]
            else:
                self.x[marble[0]].append(marble)
            if marble[1] not in self.y:
                self.y[marble[1]] = [marble]
            else:
                self.y[marble[1]].append(marble)

    def neighbors(self, marble):
        neighbors = []
        # print('getting neighbors for %s' % str(marble))
        neighbors.extend([m for m in self.x[marble[0]] +
                          self.y[marble[1]] if m != marble])
        return neighbors


def marbles_remaining(marbles: 'List[(Int, Int)]') -> 'Int':
    """Calculate remaining marbles once removal has completed

    Basic approach:
    iterate through inputs
    build graph
    traverse their graph to mark as visited
    count number of traversals that have happened
    """
    graph = AxisGraph(marbles)
    visited = set()
    marble_clusters = 0

    def _traverse_and_mark_visited(marble):
        frontier = []
        frontier.append(marble)
        visited.add(marble)

        while len(frontier) > 0:
            current_marble = frontier.pop()
            neighbors = graph.neighbors(current_marble)
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    frontier.append(neighbor)

    for marble in marbles:
        print('checking marble %s' % str(marble))
        if marble not in visited:
            print('%s not visited' % str(marble))
            _traverse_and_mark_visited(marble)
            marble_clusters += 1

    return marble_clusters


marbles = [
    (1, 3),
    (1, 5),
    (2, 4),
    (2, 8),
    (6, 1),
    (4, 3),
]

graph = AxisGraph(marbles)
# print(graph.x)
# print(graph.y)

print(marbles_remaining(marbles))
