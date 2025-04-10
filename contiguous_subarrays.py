"""This is my answer to Meta's Software Engineer, Product Preparation plan Coding exercise Contiguous Subarrays."""

def count_subarrays(arr):
  subarrays = [1] * len(arr)
  
  for index, value in enumerate(arr):
    left = index - 1
    right = index + 1

    for i in range(left, -1, -1):
      if arr[i] < value:
        subarrays[index] += 1
      else:
        break

    for i in range(right, len(arr)):
      if arr[i] < value:
        subarrays[index] += 1
      else:
        break      

  return subarrays
