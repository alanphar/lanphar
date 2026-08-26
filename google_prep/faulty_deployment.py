"""The Problem: Identifying the Faulty Deployment
You are analyzing a sequence of firmware deployments. The deployments are sequentially numbered 1 through n.

You are provided with a pre-existing API function, is_bad_deployment(version_id), which returns True if that specific version caused a critical system failure, and False if it was stable.

Because each deployment builds directly on the architecture of the previous one, if version x is bad, every single version deployed after x is also bad.

Your task is to write a function that finds the first bad deployment version in the sequence. Because querying the API is resource-heavy, your solution must minimize the number of calls made to is_bad_deployment().

Example:
Input: n = 5
is_bad_deployment(4) -> True
is_bad_deployment(3) -> False
is_bad_deployment(5) -> True

Output: 4

Assume you are writing a function def first_bad_version(n): where n is the total number of versions.
"""

def first_bad_version(versions):
   """n is the total number of versions."""
   left = 0
   right = len(versions) - 1
   first_bad = None   
 
   while left <= right:
      middle = left + (right - left)//2
      if is_bad_deployment(versions[middle]):
         first_bad = versions[middle]
         right = middle - 1
      else:
         left = middle + 1
   return first_bad

