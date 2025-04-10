"""These are my answers to Meta's Software Engineer, Product Preparation plan Coding exercise Pair sums.

First function - Brute force way, i think it is O(n^2).
Second function - Leverages hash/dict way, where O(n) memory is used to reduce time to O(n + k).
"""

def numberOfWays(arr, k):
  """Brute force way, i think it is O(n^2)."""
  number_of_ways = 0
  
  for index, number in enumerate(arr):
    for i in range(index + 1, len(arr)):
      if k - number == arr[i]:
        number_of_ways += 1

  return number_of_ways

def numberOfWays(arr, k):
  """Leveraging hash/dict way, where O(n) memory is used to reduce time to O(n + k)."""
  number_of_ways = 0
  numbers = dict()
  
  for number in arr:
    if number not in numbers:
      numbers[number] = 1
    else:
      numbers[number] += 1
      
  for attempt in range(k - 1, 0, -1):
    if attempt in numbers:
      if attempt * 2 == k:
        quantity = numbers[attempt]
        if quantity == 2:
          number_of_ways += 1
        else:
          # formula to determine valid pairs with quantity provided
          for duplicate in range(quantity):
            for _ in range(duplicate+1, quantity):
              number_of_ways += 1
      elif k - attempt in numbers:
          numbers.pop(k - attempt)
          number_of_ways += 1  

  return number_of_ways
