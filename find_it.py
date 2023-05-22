"""
Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times.
Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
"""


def count_number(seq):
    count = {}
    for number in seq:
        count[number] = count.get(number, 0) + 1
    return count


def find_it(seq):
    for number, amount in count_number(seq).items():
        if amount % 2 == 1:
            return number


def test_1():
    assert find_it([7]) == 7


def test_2():
    assert find_it([0]) == 0


def test_3():
    assert find_it([1, 1, 2]) == 2


def test_4():
    assert find_it([0, 1, 0, 1, 0]) == 0


def test_5():
    assert find_it([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]) == 4
