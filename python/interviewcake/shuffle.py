import random


def get_random(floor, ceiling):
    return random.randint(floor, ceiling)


def shuffle(numbers) -> list:
    """Shuffles a list in-place.

    Stipulation: each el in list must have equal probability of being assigned
    to each el in newlist.

    Given: get_random(floor, ceiling) fn returning a true random int.

    With a source of randomness, what is best solution?

    * Randomly assign a place, then randomly assign the nth remaining place
        with the next random int?


    Build naive solution to see shape of problem.
    Swap each number with a random place.
    """
    # naive in-place solution doesn't give true randomness
    # for i, n in enumerate(numbers):
    #     swap_slot = get_random(0, len(numbers) - 1)
    #     numbers[i] = numbers[swap_slot]
    #     numbers[swap_slot] = n

    # not in-place
    # new_list = [None] * len(numbers)
    # for i, n in enumerate(new_list):
    #     replacement = numbers.pop(get_random(0, len(numbers) - 1))
    #     new_list[i] = replacement
    # numbers = new_list

    # what is out of place solution doing?
    # taking a random list el to add
    # in-place solution?
    # not really in place if we're copying it. how to avoid?
    # keep something backwards-looking? what information do we need to track?
    # indeces of previously swapped els? that's O(n) space
    # numbers_copy = numbers.copy()
    # for i, n in enumerate(numbers):
    #     replacement = numbers_copy.pop(get_random(0, len(numbers_copy) - 1))
    #     numbers[i] = replacement

    last_idx = len(numbers) - 1
    for i, n in enumerate(numbers):
        picked_idx = get_random(i, last_idx)
        (numbers[i], numbers[picked_idx]) = (numbers[picked_idx], numbers[i])

    return len(numbers)


n = [1, 2, 3, 4, 5]
shuffle(n)
print(n)
