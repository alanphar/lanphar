"""This question was asked during a technical interview for Meta SWE Product.

Imagine you have a list of automated test results. Find the last known good version before tests began to fail.

My immediate thought in the interview was to leverage binary search to be able to have a time complexity of O(log N)
I also wanted to do the search iteratively as recursively would have a larger space complexity of O(log N)
due to call stack

Provided is a function that determines if a given version is good or bad in O(1) time.
Lets say its called is_good_version()
"""


def is_good_version(version):
    """Meta provided function determines if a given version is good or bad in O(1) time.

    I wrote this only for testing purposes. But during interview it was assumed to be a provided library function
    """
    return version == 'good'


def find_last_good_version(versions):
    """Given a list of versions, find the last good version before build started to fail.

    Returns index if it finds a last good version, otherwise returns -1.
    """
    left_pointer = 0
    right_pointer = len(versions) - 1

    while left_pointer <= right_pointer:
        pointer = (right_pointer + left_pointer) // 2

        if is_good_version(versions[pointer]):
            if pointer + 1 == len(versions):                    # last version check (right bounds check)
                return pointer
            elif not is_good_version(versions[pointer + 1]):    # last good version check
                return pointer
            left_pointer = pointer + 1
        elif pointer - 1 < 0:                                   # pointer left bounds check
            return -1
        elif is_good_version(versions[pointer - 1]):            # if current version is bad, is left closest good?
            return pointer - 1
        else:
            right_pointer = pointer - 2

    return -1


def test_find_last_good_version():
    test_case0 = []
    test_cast1 = ['good']
    test_cast2 = ['bad']
    test_cast3 = ['good', 'bad']
    test_cast4 = ['good', 'good']
    test_cast5 = ['good', 'good', 'bad']
    test_cast6 = ['good', 'good', 'good', 'bad', 'bad', 'bad', 'bad', 'bad']
    test_cases = [test_case0, test_cast1, test_cast2, test_cast3, test_cast4, test_cast5, test_cast6]

    for test in test_cases:
        print(f'Test case: {test}. Last Good Index: {find_last_good_version(test)}')


test_find_last_good_version()
