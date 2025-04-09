"""Leetcode #8 String to Integer atoi."""

def myAtoi(self, s: str) -> int:
    s = s.strip()

    if not s:
        return 0

    if s[0] == "-":
        p_flag = -1
        s = s[1:]
    elif s[0] == "+":
        p_flag = 1
        s = s[1:]
    else:
        p_flag = 1

    s = s.lstrip('0')

    result = ""

    for char in s:
        if char.isdigit():
            result += char
        else:
            break
    if result:
        total = int(result) * p_flag
        if total < -2 ** 31:
            return -2 ** 31
        elif total > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return total
    else:
        return 0
