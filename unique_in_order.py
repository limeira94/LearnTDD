"""
Implement the function unique_in_order which takes as argument a sequence and returns a list of items
without any elements with the same value next to each other and preserving the original order of elements.
Example:
    unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
    unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
    unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
    unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
"""


def unique_in_order(s):
    result = []
    for i, element in enumerate(s):
        if i == 0 or element != s[i - 1]:
            result.append(element)
    return result


def test_order_number():
    assert unique_in_order([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_order_number_2():
    assert unique_in_order([1, 2, 2, 3]) == [1, 2, 3]


def test_order_number_3():
    assert unique_in_order([1, 2, 2, 3, 2]) == [1, 2, 3, 2]


def test_order_number_4():
    assert unique_in_order([1, 2, 2, 3, 4, 3, 5, 6, 7, 7]) == [1, 2, 3, 4, 3, 5, 6, 7]


def test_order_number_with_tuple():
    assert unique_in_order((1, 2, 2, 3, 3)) == [1, 2, 3]


def test_order_char_1():
    assert unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']


def test_order_char_with_upper_and_lowercase():
    assert unique_in_order('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D']

