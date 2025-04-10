"""This is my answer to Meta's Software Engineer, Product Preparation plan Coding exercise Passing Yearbooks."""

def findSignatureCounts(arr):
   students = list(range(1, len(arr) + 1))
   signature_counts = [1] * len(arr)
  
   for student in students:
      for index in range(student - 1, -1, -1):
         if arr[index] == student:
           break
         signature_counts[student - 1] += 1
   return signature_counts
