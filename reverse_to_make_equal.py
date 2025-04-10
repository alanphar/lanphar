"""This is my answer to Meta's Software Engineer, Product Preparation plan Coding exercise Reverse to Make Equal."""

def create_dict_hash(array):
  d = dict()
  
  for number in array:
    if number in a:
      d[number] += 1
    else:
      d[number] = 1
  return d

def are_they_equal(array_a, array_b):
  """Uses the hash idea Gale talks about when discussing ransom note example during prep material to keep this at O(N)."""
  a = create_dict_hash(array_a)
  b = create_dict_hash(array_b)

  try:
    for number, quantity in a.items():
      if b[number] != quantity:
        return False
  except KeyError:
    return False

  return True
