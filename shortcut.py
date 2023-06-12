"""
Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.
Examples:
    "hello"     -->  "hll"
    "codewars"  -->  "cdwrs"
    "goodbye"   -->  "gdby"
    "HELLO"     -->  "HELLO"
"""


# def shortcut(word):
#     vowel = 'i'
#     s = ""
#     for w in word:
#         if w not in 'aeiou':
#             s += w
#     return s


def shortcut(word):
    return "".join(c for c in word if c not in "aeiou")


def test_one_vowel():
    assert shortcut("hi") == "h"

def test_two_vowel():
    assert shortcut('hello') == "hll"

def test_two_upper_vowel():
    assert shortcut("HELLO") == "HELLO"
