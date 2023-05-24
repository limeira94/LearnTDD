"""
Dada uma lista de números, retorne uma lista onde todos os elementos
adjacentes iguais são reduzidos a um único elemento

Exemplo: [1, 2, 2, 3]
Irá retornar: [1, 2, 3]
"""


def remove_adjacent(nums):

    if not nums:
        return []

    l = [nums[0]]
    for c, n in zip(nums[:-1], nums[1:]):
        if c != n:
            l.append(n)

    return l
    # return [nums[0]] + [n for c, n in zip(nums[:-1], nums[1:]) if c != n]


def test_1():
    assert remove_adjacent([1, 2, 2, 3]) == [1, 2, 3]


def test_2 ():
    assert remove_adjacent([]) == []
