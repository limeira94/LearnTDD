"""
O exercício pede para escrever uma função em Python que receba uma lista de números inteiros e um número alvo.
A função deve encontrar dois números diferentes na lista cuja soma seja igual ao número alvo. Em seguida,
os índices desses dois números devem ser retornados como uma tupla ou lista (dependendo da sua preferência).

Por exemplo, se tivermos a lista [1, 2, 3] e o número alvo for 4, a função deve retornar [0, 2] ou [2, 0],
pois os números nos índices 0 e 2 (1 e 3) somam 4.

É importante mencionar que pode haver várias respostas corretas para alguns casos de teste.
Ou seja, se houver mais de uma combinação de números que satisfaça a soma alvo, qualquer uma delas será aceita
como resposta válida.

Ex: two_sum([1, 2, 3], 4) # returns [0, 2] or [2, 0]
"""

def two_sum(numbers, target):

    seen = {}
    for index, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        seen[num] = index


def test_two_sum():
    assert two_sum([1, 2], 3) == [0, 1]

def test_two_sum_2():
    assert two_sum([1, 2, 3], 4) == [0, 2]

def test_two_sum_3():
    assert two_sum([1234, 5678, 9012], 14690) == [1, 2]


