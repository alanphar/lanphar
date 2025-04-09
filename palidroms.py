def count_palidrom(string, left, right):
    result = 0
    while left >= 0 and right < len(string) and string[left] == string[right]:
        result += 1
        left -= 1
        right += 1
    return result


def countSubstrings(s: str) -> int:
    result = 0

    for index in range(len(s)):
        result += count_palidrom(s, index, index)
        result += count_palidrom(s, index, index + 1)

    return result


def get_pali_length(s, left, right):
    pali = []
    while left >= 0 and right < len(s) and s[left] == s[right]:
        pali = s[left:right + 1]
        left -= 1
        right += 1

    return pali


def longestPalindrome(s: str) -> str:
    if len(s) == 1:
        return s

    longest = ""

    for index in range(len(s)):
        odd = get_pali_length(s, index, index)

        if len(odd) > len(longest):
            longest = odd

        even = get_pali_length(s, index, index + 1)

        if len(even) > len(longest):
            longest = even

        return longest
