def checker(number, left, right):
    while left >= 0 and right < len(number):
        if number[left] != number[right]:
            return False
        left -= 1
        right += 1
    return True


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        str_number = str(x)
        length = len(str_number)
        if length % 2 == 0:
            return checker(str_number, length // 2 - 1, length // 2)
        else:
            return checker(str_number, length // 2, length // 2)
