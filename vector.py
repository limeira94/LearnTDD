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


class Vector:
    def __init__(self, vector):
        self.vector = vector

    def add(self, outro):
        new_vector = []
        for item in range(len(self.vector)):
            soma = self.vector[item] + outro.vector[item]
            new_vector.append(soma)
        return Vector(new_vector)

    def subtract(self, outro):
        new_vector = []
        for item in range(len(self.vector)):
            subtrair = self.vector[item] - outro.vector[item]
            new_vector.append(subtrair)
        return Vector(new_vector)


def test_add_two_vector():
    a = Vector([1, 2, 3])
    b = Vector([4, 5, 6])
    vector_soma = a.add(b)
    assert vector_soma.vector == [5, 7, 9]

def test_subtract_two_vector():
    a = Vector([1, 2, 3])
    b = Vector([4, 5, 6])
    vector_sub = a.subtract(b)
    assert vector_sub.vector == [-3, -3, -3]

def test_equal_length_vector():
    a = Vector([1, 2, 3])
    b = Vector([4, 5, 6])
    vetor_soma = a.subtract(b)
    assert vetor_soma.vector ==