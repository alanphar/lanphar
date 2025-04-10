"""Merge sort uses recursion to improve time to O(nlogn)."""


def merge_array_element1(target_array, array):
    """Inserts array[0] at the end of target_array."""
    target_array.append(array[0])
    array.pop(0)


def merge_sorted_arrays(left_array, right_array):
    """Takes two sorted arrays and merges them into one sorted array."""
    new_array = []
    while left_array and right_array:
        if left_array[0] <= right_array[0]:
            merge_array_element1(new_array, left_array)
        else:
            merge_array_element1(new_array, right_array)

    while left_array:
        merge_array_element1(new_array, left_array)

    while right_array:
        merge_array_element1(new_array, right_array)

    return new_array


def sort(array):
    """Merge sort uses recursion to improve time to O(nlogn).

    Uses divide and conquer approach
    """
    length = len(array)
    if length == 1:
        return array

    mid = length // 2
    left_array = sort(array[:mid])
    right_array = sort(array[mid:])
    return merge_sorted_arrays(left_array, right_array)
