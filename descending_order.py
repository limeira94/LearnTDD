"""
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in
descending order. Essentially, rearrange the digits to create the highest possible number.
Examples:
Input: 42145 Output: 54421
Input: 145263 Output: 654321
Input: 123456789 Output: 987654321

What tests do I need to do?
1. Are in descending form with 1 number
2. 2 numbers
3. Many numbers
"""


def descending_order(number):
    return int(''.join(sorted(str(number), reverse=True)))


def test_1_number():
    assert descending_order(1) == 1


def test_2_numbers():
    assert descending_order(12) == 21


def test_many_numbers():
    assert descending_order(123) == 321


def test_order_difference_number():
    assert descending_order(435) == 543
    assert descending_order(6576334) == 7665433

