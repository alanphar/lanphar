"""machineCapacity is a parameter list of size n. Each individual machine’s capacity is
 an integer value in the array. The efficiency is evaluated using a comparison metric:
 the sum of the absolute difference between consecutive machine capacities.
 The task is to determine whether achieving the same sum of absolute difference is possible
 by removing some machines from the sequence to streamline the operations.
 If it is possible, return the minimum number of machines required in the sequence
 to attain the same sum of the absolute difference between consecutive machine capacities.
"""


def min_machines_for_same_efficiency(machineCapacity):
    n = len(machineCapacity)
    if n <= 2:
        return n  # Trivial case: can't remove anything

    original_efficiency = sum(abs(machineCapacity[i+1] - machineCapacity[i]) for i in range(n - 1))

    # Always keep the first machine
    streamlined = [machineCapacity[0]]

    for i in range(1, n - 1):
        a = streamlined[-1]
        b = machineCapacity[i]
        c = machineCapacity[i + 1]
        # Check if b is redundant (can be removed without changing efficiency)
        if abs(a - b) + abs(b - c) != abs(a - c):
            streamlined.append(b)

    # Always keep the last machine
    streamlined.append(machineCapacity[-1])

    # Check if efficiency of new sequence matches original
    new_efficiency = sum(abs(streamlined[i+1] - streamlined[i]) for i in range(len(streamlined) - 1))
    if new_efficiency == original_efficiency:
        return len(streamlined)
    else:
        return n  # No machine can be removed

# Example usage
machine_capacity = [5,4,0,3,3,1]
print(min_machines_for_same_efficiency(machine_capacity))
