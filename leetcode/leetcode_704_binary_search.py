"""This was my first recursive and correct attempt at LeetCode's 704. Binary Search question.

a better solution that is iterative is in my binary_search.py
"""

class Solution:
    def search(self, nums, target: int) -> int:
        length = len(nums)
        if length == 0:
            return -1
        if length == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        targeted_index = length//2
        if target == nums[targeted_index]:
            return targeted_index
        elif target < nums[targeted_index]:
            return self.search(nums[:targeted_index], target)
        elif target > nums[targeted_index]:
            temp = self.search(nums[targeted_index+1:], target)
            if temp != -1:
                return temp + len(nums[:targeted_index]) + 1
        return -1
