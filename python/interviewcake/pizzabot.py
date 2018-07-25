"""
Pizzabot

Input:
5x5 (0, 0) (1, 3) (4, 4) (4, 2) (4, 2) (0, 1) (3, 2) (2, 3) (4, 1)

Output primitives:
N: Move north
S: Move south
E: Move east
W: Move west
D: Drop pizza
"""

import unittest


def show(grid, cc):
    drawing = ''

    def _sq(q, a, b):
        return 'X' if a == cc[0] and b == cc[1] else str(q)

    for y, row in enumerate(grid):
        drawing += '|'.join([_sq(s, x, y) for (x, s) in enumerate(row)])
        drawing += '\n'
    print(drawing)


def navigate(grid):
    directions = ''
    is_eastbound = True

    x = 0
    y = 0
    while y < len(grid):
        while ((is_eastbound and x < len(grid[y])) or
               ((not is_eastbound) and x >= 0)):
            if grid[y][x]:
                directions += 'D'
                print('DROP:')
                show(grid, (x, y))
            if is_eastbound:
                directions += 'E'
                x += 1
            else:
                directions += 'W'
                x -= 1
        directions += 'S'
        x += -1 if is_eastbound else 1
        is_eastbound = not is_eastbound
        y += 1
    return directions[:-1]


def read(coords):
    grid = []
    for y in range(5):
        grid.append([])
        for x in range(5):
            grid[y].append(0)
    for c in coords:
        grid[c[1]][c[0]] = 1
    return grid


def run(coordinates):
    return navigate(read(coordinates))


class Test(unittest.TestCase):

    GRID = [(0, 0), (1, 3), (4, 4), (4, 2), (4, 2),
            (0, 1), (3, 2), (2, 3), (4, 1)]

    def test_merge_ranges(self):
        print('\n')
        self.assertEqual(
            run(self.GRID), "DEEEEESDWWWWDWSEEEDEDESWWDWDWWSEEEEDE")


unittest.main(verbosity=2)
