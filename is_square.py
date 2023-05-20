"""
Given an integral number, determine if it's a square number:
Examples:
    -1  =>  false
     0  =>  true
     3  =>  false
     4  =>  true
    25  =>  true
    26  =>  false
What test do I need to take?
    1. test the number 0
    2. test the square number
    3. test a non-square number
    4. test a negative number
"""


def is_square(number):
    if number < 0:
        return False
    if number == 0:
        return True
    i = 1
    while i * i <= number:
        if i * i == number:
            return True
        i += 1
    return False


def test_square_9():
    assert is_square(9) == True


def test_square_4():
    assert is_square(4) == True


def test_square_0():
    assert is_square(0) == True


def test_square_3():
    assert is_square(3) == False


def test_negative_number():
    assert is_square(-1) == False


def test_big_numer():
    assert is_square(2500) == True