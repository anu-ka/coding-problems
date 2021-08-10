# https://leetcode.com/problems/rotate-string/
# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
# A shift on s consists of moving the leftmost character of s to the rightmost position.
# For example, if s = "abcde", then it will be "bcdea" after one shift.

import pytest


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        length = len(s)
        for i in range(1, length + 1):
            if goal[i:length] + goal[0:i] == s:
                return True

        return False


@pytest.mark.parametrize(
    ("s", "goal", "result"),
    [
        ("abcde", "cdeab", True),
        ("abcde", "abced", False),
        ("ckahkzpikz", "hkzpikzcka", True),
    ],
)
def test_basic(s: str, goal: str, result: bool) -> None:
    assert result == Solution().rotateString(s, goal)
