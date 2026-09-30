Binary search is an efficient search algorithm for sorted arrays. In Python, the bisect module can be used for binary search. The bisect.bisect() function finds the position of the number in the list or a place for the number if it is not present. The bisect.bisect_left() function does the same, but carefully chooses its insertion point to the left of any existing entries of the same value.

For example, to search for an element in a list, one can use the following code:

import bisect

def binary_search(list, item):
    pos = bisect.bisect_left(list, item)
    if pos != len(list) and list[pos] == item:
        return pos
    else:
        return -1

list = [1, 2, 4, 7, 8]
print(binary_search(list, 2))  # Outputs 1