"""Heap practice."""


def heapify(array):
   """Implement using Floyd’s algorithm for O(n) creation of a heap."""
   starting_index = len(array) // 2 - 1
   
   for index in range(starting_index, -1, -1):
       shift_down(index, array)


def shift_down(index, array):
    while True:
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest_index = index
        
        if left_child_index < len(array) and array[smallest_index] > array[left_child_index]:
            smallest_index = left_child_index
            
        if right_child_index < len(array) and array[smallest_index] > array[right_child_index]:
            smallest_index = right_child_index
            
        if smallest_index == index:
            break
            
        array[index], array[smallest_index] = array[smallest_index], array[index]
        
        index = smallest_index
               
