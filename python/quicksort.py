
# def quicksort(numbers, start=0, end=0):
#     def _partition(a, b):

#         fulcrum = numbers[b]
#         dep_idx = a - 1

#         for i in range(a, b - 1):
#             if numbers[i] <= fulcrum:
#                 dep_idx += 1
#                 (numbers[dep_idx], numbers[i]) = (numbers[i], numbers[dep_idx])

#         (numbers[dep_idx + 1], numbers[b]) = (numbers[b], numbers[dep_idx + 1])
#         return dep_idx + 1

#     if start < end:
#         fulcrum = _partition(start, end)
#         quicksort(numbers, start, fulcrum - 1)
#         quicksort(numbers, fulcrum + 1, end)

#     return numbers

# a = [7,5,4,5762,462,6,6,237,2,5,8]
# print(quicksort(a, 0, len(a) - 1))


def quicksort(a_list, start=0, end=0):
    """Order a list in-place.

    Basic strategy:
        define an arbitrary partition.
        swap numbers less than the partition element left of it
        repeat operation on both sides of the partition
    """

    def _partition(p, r):
        fulcrum = a_list[r]
        i = p - 1

        for j in range(p, r):
            if a_list[j] < fulcrum:
                i += 1
                a_list[i], a_list[j] = a_list[j], a_list[i]

        a_list[i + 1], a_list[r] = a_list[r], a_list[i + 1]

        return i + 1

    if start < end:
        fulcrum = _partition(start, end)
        quicksort(a_list, start, fulcrum - 1)
        quicksort(a_list, fulcrum + 1, end)

    return a_list

a = [7,5,4,5762,462,6,6,237,2,5,8]
print(quicksort(a, 0, len(a) - 1))

b = [36, 11, 42, 24, 31, 12, 11, 32, 1, 27, 6, 39, 4, 12, 18, 13, 39, 21, 26, 1]
print(quicksort(b, 0, len(b) - 1))
