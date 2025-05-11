"""Given a list of powers of n number of servers as an array of integers,
find the maximum number of servers that can be selected from a set of servers
that can be rearranged in a way that the absolute difference between power of two
adjacent servers is equal to or less than 1. The first and last servers in the sequence
are also considered adjacent.
Powers can be duplicates.
The function should be called getMaxServers that takes an array called powers."""
from itertools import permutations


def is_valid_circle(arr):
    n = len(arr)
    for i in range(n):
        if abs(arr[i] - arr[(i + 1) % n]) > 1:
            return False
    return True


def get_max_servers(powers):
    n = len(powers)

    for size in range(n, 0, -1):  # Start from largest size
        for subset in permutations(powers, size):
            if is_valid_circle(subset):
                return size  # Early return for largest possible subset
    return 0


# Example usage
powers = [2,2,3,2,1,2,2]
print(get_max_servers(powers))
