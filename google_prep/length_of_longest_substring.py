"""The standard practice for sliding windows is to measure th ewindow at the bottom of every interation."""

def length_of_longest_substring(s):
   longest = left = 0
   found_characters = dict()   

   for index, character in enumerate(s):
      if character in found_characters and found_characters[character] >= left:
         left = found_characters[character] + 1
      
      found_characters[character] = index
      longest = max(longest, index - left + 1)

   return longest

