"""implements iterative binary search of a sorted array to save space as recursively uses O(n) memory."""


def binary_search(array, target):
    """returns index of target otherwise -1."""
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (right + left) // 2
        if array[middle] == target:
            return middle
        if array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1
