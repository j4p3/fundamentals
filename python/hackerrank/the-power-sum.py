#!/bin/python3

import math
import os
import random
import re
import sys

set = lambda X, N: [i**N for i in range(math.floor(X**(1/N)))]

def powerSum(X, N):
    # find unique solutions
    #   find a solution
    # 

    # set of integers lte root(X)
    # square value of each integer in set
    # play with blocks
    # 
    # how to recurse to find combinations? state in tree? recurse over loop adding nodes to tree, checking to see if path has overshot or equalled target?
    # 
    solutions = []
    combo = []
    for item in set(X, N):
        print(item)
        if (sum(combo) == X):
            solutions.append(combo)
        elif (sum(combo) + item < X):
            combo.append(item)

    # count unique solutions
    return N

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input())

    N = int(input())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
