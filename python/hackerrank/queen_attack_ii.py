#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the queensAttack function below.
def queensAttack(n: 'int: board size',
                 k: 'int: # obstacles',
                 r_q: 'int: queen row',
                 c_q: 'int: queen column',
                 obstacles: 'list: (row, column)') -> int:
    """Sum total of squares currently attackable by queen.

    Strategies:
    * define [[]] for board, iterate, test for queen attack
    * calculate total attackable space, account for blockages
    * iterate across attackble space until blockage or end of board encountered

    Do we need to build a board, or can we just look up obstacles?
    """

    ATTACK_VECTORS = [(1, 0),
                      (1, -1),
                      (0, -1),
                      (-1, -1),
                      (-1, 0),
                      (-1, 1),
                      (0, 1),
                      (1, 1)]

    obstacles_map = {}
    for obstacle in obstacles:
        if obstacle[1] in obstacles_map:
            obstacles_map[obstacle[1]][obstacle[0]] = True
        else:
            obstacles_map[obstacle[1]] = {obstacle[0]: True}

    attackable_squares = 0

    for vector in ATTACK_VECTORS:
        position = [c_q + vector[0], r_q + vector[1]]

        while position[0] > 0 and position[0] <= n and \
                position[1] > 0 and position[1] <= n and \
                not (position[0] in obstacles_map and
                     position[1] in obstacles_map[position[0]]):
            attackable_squares += 1
            position[0] += vector[0]
            position[1] += vector[1]
        # print('vector %s terminated at position %s' % (str(vector), str(position)))

    return attackable_squares


def test_for_squares(obstacles):
    for obstacle in obstacles:
        if obstacle[0] == obstacle[1]:
            print(obstacle)


if __name__ == '__main__':
    print('running queen_attack_ii')

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
