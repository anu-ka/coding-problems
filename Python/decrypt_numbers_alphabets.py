# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
# Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

# Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
# Return the string formed after mapping.

# It's guaranteed that a unique mapping will always exist.
import pytest


class Solution:
    def freqAlphabets(self, s: str) -> str:
        dict_numbers = {
            1: "a",
            2: "b",
            3: "c",
            4: "d",
            5: "e",
            6: "f",
            7: "g",
            8: "h",
            9: "i",
            10: "j",
            11: "k",
            12: "l",
            13: "m",
            14: "n",
            15: "o",
            16: "p",
            17: "q",
            18: "r",
            19: "s",
            20: "t",
            21: "u",
            22: "v",
            23: "w",
            24: "x",
            25: "y",
            26: "z",
        }
        i = 0
        result = ""
        while i < len(s):
            if i < len(s) - 2 and s[i + 2] == "#":
                p = s[i : i + 2]
                i += 3
            else:
                p = s[i]
                i += 1

            result += dict_numbers[int(p)]
        return result


@pytest.mark.parametrize(
    ("s", "result"),
    [
        ("10#11#12", "jkab"),
        ("1326#", "acz"),
        ("25#", "y"),
        (
            "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#",
            "abcdefghijklmnopqrstuvwxyz",
        ),
    ],
)
def test_basic(s: str, result: str) -> None:
    assert result == Solution().freqAlphabets(s)
