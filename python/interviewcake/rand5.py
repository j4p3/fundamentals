import random
import math


def rand7():
    """returns a random string between one and seven"""
    return random.randrange(1, 8)


def rand5():
    """returns a random string between one and five"""
    rands = [rand7() for i in range(5)]
    print(rands)
    return sum(rands) % 5 + 1


print(rand5())
