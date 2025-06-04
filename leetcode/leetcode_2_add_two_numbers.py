# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_number(linked_list):
    total = 0
    multiplier = 1

    while linked_list:
        total += linked_list.val * multiplier
        multiplier *= 10
        linked_list = linked_list.next

    return total


def get_linked_list(number):
    str_number = str(number)
    previous = ListNode(int(str_number[0]))
    for digit in str_number[1:]:
        num = ListNode(int(digit))
        num.next = previous
        previous = num
    return previous


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first_number = get_number(l1)
        second_number = get_number(l2)

        return get_linked_list(first_number + second_number)
