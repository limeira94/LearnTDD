"""
Make a program that filters a list of strings and returns a list with only your friends name in it.
If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure
he's not...
Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
"""


def friends(names):
    return [word for word in names if len(word) == 4]


def test_1_friend():
    assert friends(["Ryan"]) == ["Ryan"]
    assert friends(["Yous"]) == ["Yous"]


def test_2_friends():
    assert friends(["Ryan", "Yous"]) == ["Ryan", "Yous"]


def test_2_friend_dif():
    assert friends(["Ryan", "Jason"]) == ["Ryan"]
    assert friends(["Yous", "Jason"]) == ["Yous"]


def test_4_fiends():
    assert friends(["Ryan", "Kieran", "Jason", "Yous"]) == ["Ryan", "Yous"]
