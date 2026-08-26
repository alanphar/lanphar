"""Heap practice.

Below is an implementation of min heap using python list
"""


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
               

def insert(array, item):
   array.append(item)
   shift_up(len(array)-1, array)

def shift_up(index, array):
   while True:
      parent = (index - 1) // 2

      if index > 0 and array[parent] > array[index]:
         array[parent], array[index] = array[index], array[parent]
         index = parent
      else:
         break

def delete(array):
   top = array[0]
   array[0] = array.pop()
   shift_down(0, array)
   return top
      
