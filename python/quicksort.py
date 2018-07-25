
def quicksort(numbers, start=0, end=0):
    def _partition(a, b):

        fulcrum = numbers[b]
        dep_idx = a - 1

        for i in range(a, b - 1):
            if numbers[i] <= fulcrum:
                dep_idx += 1
                (numbers[dep_idx], numbers[i]) = (numbers[i], numbers[dep_idx])

        (numbers[dep_idx + 1], numbers[b]) = (numbers[b], numbers[dep_idx + 1])
        return dep_idx + 1

    if start < end:
        fulcrum = _partition(start, end)
        quicksort(numbers, start, fulcrum - 1)
        quicksort(numbers, fulcrum + 1, end)

    return numbers

a = [7,5,4,5762,462,6,6,237,2,5,8]
print(quicksort(a, 0, len(a) - 1))
