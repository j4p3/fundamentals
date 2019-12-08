from collections import deque
import heapq


class Queue:
    """Basic queue.

    Thin wrapper around deque.
    Could/should be a priority queue for optimized traversals.
    Would need a heap of priority-ordered tuples instead of deque.
    """
    def __init__(self):
        self.els = deque()

    def empty(self):
        return len(self.els) == 0

    def put(self, el):
        self.els.append(el)

    def get(self):
        return self.els.popleft()


class PriorityQueue:
    """Prioritized queue of tuples.
    """
    def __init__(self):
        self.els = []

    def is_empty(self):
        return len(self.els) == 0

    def put(self, el, priority):
        heapq.heappush(self.els, (priority, el))

    def get(self):
        return heapq.heappop(self.els)[1]


class Graph:
    """Simple graph storing edges (rather than nodes).
    """
    def __init__(self):
        self.edges = {}

    def neighbors(self, id):
        return self.edges.get(id)


class GridGraph:
    """Simple unweighted grid graph with support for disconnected nodes (walls)
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

    def is_in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def is_passable(self, id):
        return id not in self.walls

    def neighbors(self, id):
        (x, y) = id
        neighbors = [(x+1, y), (x, y-1), (x-1, y), (x+1, y+1)]
        neighbors = filter(self.is_in_bounds, neighbors)
        neighbors = filter(self.is_passable, neighbors)
        return neighbors


class WeightedGridGraph(GridGraph):
    """Weighted grid graph with support for walls
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        self.weights = {}

    def cost(self, id):
        """Cost of moving along an edge

        Note: this graph stores edges. It's actually a grid of edges.
        Nodes don't have costs, the spaces between nodes have costs.
        This method could be implemented with a from_node and a to_node.
        """
        return self.weights.get(id)


class GraphNode:
    """Simple graph node.

    Not necessary for use in above Graph class,
    which uses primitives for nodes.
    """
    def __init__(self, val):
        self.val = val
        self.neighbors = set()

    def __str__(self):
        return '%s' % self.val

    def __repr__(self):
        return self.__str__()


def dfs(graph: 'Dict', node: 'Node', target: 'Node') -> 'List[Node]':
    """Find path from node to destination, not necessarily shortest

    * DFS lends itself well to recursion
    * DFS iterative uses stack instead of queue
    """
    path = []
    nodes_to_visit = [node]
    path_map = {node: None}
    current_node = node

    while current_node != target:
        current_node = nodes_to_visit.pop()

        for neighbor in graph[current_node]:
            if neighbor not in path_map:
                path_map[neighbor] = current_node
                nodes_to_visit.append(neighbor)

    if current_node != target:
        return None

    return current_node

    while current_node:
        path.append(current_node)
        current_node = path_map[current_node]

    path.reverse()
    return path


def bfs(graph: 'Dict', node: 'Node', target: 'Node') -> 'List[Node]':
    """Find a path from node to destination

    * BFS is always going to involve pushing nodes into a queue
    * then dequeuing them and doing something to them
    *   i.e. check for target or enqueue neighbors/children
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

    return current_node

    while current_node:
        path.append(current_node)
        current_node = path_map[current_node]

    path.reverse()
    return path


def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.is_empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far


g = {
            'a': ['b', 'c', 'd'],
            'b': ['a', 'd'],
            'c': ['a', 'e'],
            'd': ['a', 'b'],
            'e': ['c'],
            'f': ['g'],
            'g': ['f'],
        }
print(dfs(g, 'a', 'e'))
