# https://leetcode.com/problems/consecutive-characters/
# The power of the string is the maximum length of a non-empty substring that
# contains only one unique character.
# Given a string s, return the power of s.

import pytest


class Solution:
    def maxPower(self, s: str) -> int:
        count = 1
        i = 0
        while i < len(s):
            j = i + 1
            c = 1
            while j < len(s) and s[i] == s[j]:
                c += 1
                i += 1
                j += 1
            if count < c:
                count = c
            i += 1
        return count


@pytest.mark.parametrize(
    ("s", "result"),
    [("cc", 2), ("leetcode", 2), ("ccbccbb", 2), ("hooraaaaaaaaaaay", 11)],
)
def test_maxPower(s: str, result: int) -> None:
    assert result == Solution().maxPower(s)
