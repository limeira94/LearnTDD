"""
Write a function that accepts an array of 10 integers (between 0 and 9),
that returns a string of those numbers in the form of a phone number.
Example:
    create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
"""


def create_phone_number(n):
    s = ''.join(map(str, n))
    return f"({s[:3]}) {s[3:6]}-{s[6:]}"


def test_create_number():
    assert create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"

