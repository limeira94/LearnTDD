"""
Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the
missing second character of the final pair with an underscore ('_').
Example:
* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""


def solution(s):

    result = []
    for i in range(0, len(s), 2):
        if len(s) % 2 == 0:
            result.append(s[i:i+2])
        else:
            s += '_'
            result.append(s[i:i+2])
    return result


def test_one_char():
    assert solution('a') == ['a_']


def test_two_char():
    assert solution("ab") == ["ab"]


def test_tree_char():
    assert solution("abc") == ["ab", "c_"]


def test_four_char():
    assert solution("abcd") == ["ab", "cd"]


def test_five_char():
    assert solution("abcde") == ["ab", "cd", "e_"]


def test_six_char():
    assert solution("abcdef") == ["ab", "cd", "ef"]


def test_seven_char():
    assert solution("abcdefg") == ["ab", "cd", "ef", "g_"]


def test_empty():
    assert solution("") == []
