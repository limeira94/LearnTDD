"""
Your Job
Find the sum of all multiples of n below m

Keep in Mind
n and m are natural numbers (positive integers)
m is excluded from the multiples

Examples:
    sumMul(2, 9)   ==> 2 + 4 + 6 + 8 = 20
    sumMul(3, 13)  ==> 3 + 6 + 9 + 12 = 30
    sumMul(4, 123) ==> 4 + 8 + 12 + ... = 1860
    sumMul(4, -7)  ==> "INVALID"
"""

def sum_mul(n, m):
    if m < 0 or n <= 0:
        return 'INVALID'
    return sum([i for i in range(n, m, n)])

def sum_mul2(n, m):
    if m < 0 or n <= 0:
        return 'INVALID'
    sum = 0
    for i in range(n, m, n):
        sum += i
    return sum

def test_one_to_five():
    assert sum_mul(1, 5) == 10

def test_two_to_nine():
    assert sum_mul(2, 9) == 20

def test_three_to_thirteen():
    assert sum_mul(3, 13) == 30

def test_negative():
    assert sum_mul(4, -7) == 'INVALID'
