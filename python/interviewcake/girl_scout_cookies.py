"""
Sorted array merging - can be done in O(n) since arrays are presorted.

Easy with known number of arrays. What about unknown number? Need to keep a
 variable tracker instead of hard-coding it. Would a tree help?
 Probably nlog(n) because of search on each insertion.
"""

my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]
third_list = [3, 5, 6, 9, 23, 25, 25]
another_list = [6, 7, 1, 2, 2, 1, 5, 0, 6]


def merge_lists(a_list, b_list):
    return sorted(a_list + b_list)


def merge_lists_2(a_list, b_list):
    c_list = []
    a_idx = b_idx = 0
    while a_idx < len(a_list) or b_idx < len(b_list):
        if (not a_idx >= len(a_list) and
                (b_idx >= len(b_list) or
                 a_list[a_idx] < b_list[b_idx])):
            c_list.append(a_list[a_idx])
            a_idx += 1
        else:
            c_list.append(b_list[b_idx])
            b_idx += 1
    return c_list


def merge_multiple_lists(lists):
    trackers = [{'idx': 0, 'l': len(list)} for list in lists]
    output = []

    while not all(map(lambda l: l['idx'] >= l['l'], trackers)):
        next_items = [lists[i][t['idx']] if t['idx'] < t['l']
                      else float('inf') for (i, t) in enumerate(trackers)]
        list_with_least = next_items.index(min(next_items))
        output.append(lists[list_with_least][trackers[list_with_least]['idx']])
        print('added %d from list %d' % (
            lists[list_with_least][trackers[list_with_least]['idx']], list_with_least))
        trackers[list_with_least]['idx'] += 1
    return output


print(merge_lists(my_list, alices_list))
print(merge_lists_2(my_list, alices_list))
print(merge_multiple_lists([my_list, alices_list,
                            sorted(third_list), sorted(another_list)]))
