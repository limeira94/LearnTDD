"""
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
which is the number of times you must multiply the digits in num until you reach a single digit.
For example (Input --> Output):
    39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
    999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
    4 --> 0 (because 4 is already a one-digit number)
"""


def persistence(n):

    lista = []
    temp = n
    while temp > 0:
        digit1 = temp % 10
        digit2 = temp // 10
        result = digit1 * digit2
        lista.append(result)
        temp = result

    return len(lista) - 1


# def test_one_digit():
#     assert persistence(4) == 0
#
# def test_two_digits():
#     assert persistence(12) == 1
#
# def test_two_digits_2():
#     assert persistence(39) == 3

def test_three_digits():
    assert persistence(999) == 4
