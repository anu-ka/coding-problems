# https://leetcode.com/problems/backspace-string-compare/
# Given two strings s and t,
# return true if they are equal when both are typed into empty text editors.
# '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.

import pytest


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_list = self.removeBackspace(s)
        t_list = self.removeBackspace(t)
        return s_list == t_list

    def removeBackspace(self, s: str) -> list[str]:
        list_chars = []
        for i in s:
            if i == "#":
                try:
                    list_chars.pop()
                except IndexError:
                    pass
            else:
                list_chars.append(i)

        return list_chars


@pytest.mark.parametrize(
    ("s", "t", "result"),
    [("ab#c", "ad#c", True), ("a#c", "d#d", False), ("#a", "a#a", True)],
)
def test_basic(s: str, t: str, result: bool) -> None:
    assert result == Solution().backspaceCompare(s, t)
