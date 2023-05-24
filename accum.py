"""
This time no story, no theory. The examples below show you how to write function accum:
Examples:
    accum("abcd") -> "A-Bb-Ccc-Dddd"
    accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
    accum("cwAt") -> "C-Ww-Aaa-Tttt"
    The parameter of accum is a string which includes only letters from a..z and A..Z.
"""


def accum(s):
    texto = ""
    for i in range(len(s)):
        texto += ((i + 1) * s[i]).capitalize() + '-'
    return texto[:-1]


def test_seven_letter():
    assert accum("RqaEzty") == "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"


def test_three_letter():
    assert accum("abc") == "A-Bb-Ccc"


def test_two_letter():
    assert accum("ab") == "A-Bb"


def test_one_letter():
    assert accum("a") == "A"
