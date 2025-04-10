"""A popular sorting algorithm however its O(n^2)."""


def sort(array):
    length = len(array)
    for i in range(length):
        for index in range(length - 1 - i):
            if array[index] > array[index + 1]:
                temp = array[index]
                array[index] = array[index + 1]
                array[index + 1] = temp
    return array
