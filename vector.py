"""
Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:
Example:
a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

a.add(b)      # should return a new Vector([4, 6, 8])
a.subtract(b) # should return a new Vector([-2, -2, -2])
a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
a.add(c)      # raises an exception

If you try to add, subtract, or dot two vectors with different lengths, you must throw an error!

Also provide:

a toString method, so that using the vectors from above, a.toString() === '(1,2,3)' (in Python, this is a __str__ method, so that str(a) == '(1,2,3)')
an equals method, to check that two vectors that have the same components are equal
"""
import pytest
from math import sqrt

class Vector:
    def __init__(self, components):
        self.components = components

    def __str__(self):
        return '(' + ','.join(str(c) for c in self.components) + ')'

    def equals(self, other):
        return self.components == other.components

    def add(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same length")
        result = []
        for item in range(len(self.components)):
            soma = self.components[item] + other.components[item]
            result.append(soma)
        return Vector(result)

    def subtract(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same length")
        result = []
        for item in range(len(self.components)):
            subt = self.components[item] - other.components[item]
            result.append(subt)
        return Vector(result)

    def dot(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same length")
        result = 0
        for vec in zip(self.components, other.components):
            mult = vec[0] * vec[1]
            result += mult
        return result

    def norm(self):
        result = 0
        for vec in self.components:
            exp = vec ** 2
            result += exp
        return sqrt(result)


def test_norm_two_vector():
    a = Vector([1, 2, 3])
    assert a.norm() == sqrt(14)

def test_dot_two_vector():
    a = Vector([1, 2, 3])
    b = Vector([4, 5, 6])
    assert a.dot(b) == 32

def test_add_two_vector():
    a = Vector([1, 2, 3])
    b = Vector([4, 5, 6])
    vector_soma = a.add(b)
    assert vector_soma.components == [5, 7, 9]

def test_subtract_two_vector():
    a = Vector([1, 2, 3])
    b = Vector([4, 5, 6])
    vector_sub = a.subtract(b)
    assert vector_sub.components == [-3, -3, -3]

def test_length_diff():
    a = Vector([1, 2, 3])
    b = Vector([4, 5, 6, 7])
    with pytest.raises(ValueError):
        a.add(b)
