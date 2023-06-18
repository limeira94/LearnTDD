"""
Given two arrays a and b write a function comp(a, b) that checks whether the two
arrays have the "same" elements, with the same multiplicities
(the multiplicity of a member is the number of times it appears).
"Same" means, here, that the elements in b are the elements in a squared, regardless of the order.
Examples:
    Valid arrays
    a = [121, 144, 19, 161, 19, 144, 19, 11]
    b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

    a = [121, 144, 19, 161, 19, 144, 19, 11]
    b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

    Invalid arrays
    a = [121, 144, 19, 161, 19, 144, 19, 11]
    b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
    comp(a,b) returns false because in b 132 is not the square of any number of a
"""


def comp(a, b):
    return len(a) == len(b) and all(x * x in b for x in a)

def comp2(a, b):

    if len(a) == len(b):
        for x in a:
            if x ** 2 not in b:
                return False
        return True

def test_one_number():
    a = [3]
    b = [9]
    assert comp(a, b) == True

def test_two_numbers():
    a = [3, 4]
    b = [9, 16]
    assert comp(a, b) == True

def test_two_numbers_out_of_order():
    a = [3, 4]
    b = [16, 9]
    assert comp(a, b) == True

def test_three_numbers():
    a = [3, 4, 5]
    b = [9, 16, 25]
    assert comp(a, b) == True

def test_three_numbers_not_exact_square():
    a = [3, 4, 5]
    b = [10, 17, 26]
    assert comp(a, b) == False

def test_one_number_not_square():
    a = [3, 4, 5]
    b = [9, 17, 36]
    assert comp(a, b) == False
