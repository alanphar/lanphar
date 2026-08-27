class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        """Window size is used to determine contiguous days."""
        left = count = 0

        for index in range(len(prices)):
            if index > 0 and prices[index - 1] - prices[index] != 1: # streak broken
                left = index

            count += index - left + 1
            
        return count
