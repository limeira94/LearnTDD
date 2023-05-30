"""
Dado um contador de inteiros, retorne uma string 'Number of donuts: <count>', onde
é o número recebido, caso o contador for 10 ou mais retorne 'Number of donuts: <many>'
"""


def donuts(count, limit=10):
    return f'Number of donuts: {Quantity(count)}'


class Quantity:

    def __init__(self, count, limit=10):
        self.count = count
        self.limit = limit

    @property
    def many(self):
        return self.count >= self.limit

    def __str__(self):
        return 'many' if self.many else str(self.count)


def test_quantity():
    assert Quantity(5)
    assert str(Quantity(5)) == '5'
    assert str(Quantity(10)) == 'many'


def test_donuts():
    assert donuts(5), 'Number of donuts: 5'
    assert donuts(10), 'Number of donuts: many'
