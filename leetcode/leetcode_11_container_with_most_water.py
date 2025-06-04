class Solution:
    def maxArea(self, height) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            length = right - left
            max_area = max(max_area, min(height[left], height[right]) * length)
            if height[left] > height[right]:
                right -= 1
            elif height[left] < height[right]:
                left += 1
            else:
                right -= 1
                left += 1

        return max_area