# You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd indices.
# There is a function shift(c, x), where c is a character and x is a digit,
# that returns the xth character after c.
# For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
# For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]).
# Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.
# https://leetcode.com/problems/replace-all-digits-with-characters/

import pytest


class Solution:
    def replaceDigits(self, s: str) -> str:
        refer = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]
        result = ""
        i = 0
        while i < len(s):
            character = s[i]
            if i + 1 < len(s):
                num = int(s[i + 1])
                step = refer.index(character)
                step += num
                result = result + character + refer[step]
            else:
                result = result + character
            i += 2
        return result


@pytest.mark.parametrize(
    ("s", "expected"), [("a1b2c3d4e", "abbdcfdhe"), ("a1b1c1", "abbccd")]
)
def test_basic(s: str, expected: str):
    assert expected == Solution().replaceDigits(s)
