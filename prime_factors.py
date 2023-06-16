"""
Inspired by one of Uncle Bob's TDD Kata
Write a function that generates factors for a given number.
The function takes an integer as parameter and returns a list of integers
(ObjC: array of NSNumbers representing integers). That list contains the prime factors in numerical sequence.
Examples:
    1  ==>  []
    3  ==>  [3]
    8  ==>  [2, 2, 2]
    9  ==>  [3, 3]
    12 ==>  [2, 2, 3]
"""


def prime_factors(n):

    factor = []
    div = 2
    while div <= n:
        if n % div == 0:
            n /= div
            factor.append(div)
        else:
            div += 1
    return factor


def test_one():
    assert prime_factors(1) == []

def test_three():
    assert prime_factors(3) == [3]

def test_eight():
    assert prime_factors(8) == [2, 2, 2]

def test_nine():
    assert prime_factors(9) == [3, 3]

def test_twelve():
    assert prime_factors(12) == [2, 2, 3]