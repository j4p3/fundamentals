#!/bin/python3

import os
import sys
from functools import reduce

j = lambda c: (1 if c[0]>c[1] else 0, 1 if c[1]>c[0] else 0)

def solve(a0, a1, a2, b0, b1, b2):
    chals = zip((a0,a1,a2), (b0,b1,b2))
    return reduce(lambda s, c: (s[0] + j(c)[0], s[1] + j(c)[1]), chals, [0,0])


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    a0A1A2 = input().split()

    a0 = int(a0A1A2[0])

    a1 = int(a0A1A2[1])

    a2 = int(a0A1A2[2])

    b0B1B2 = input().split()

    b0 = int(b0B1B2[0])

    b1 = int(b0B1B2[1])

    b2 = int(b0B1B2[2])

    result = solve(a0, a1, a2, b0, b1, b2)

    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()
