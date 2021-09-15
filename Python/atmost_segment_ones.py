# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/
# Given a binary string s ​​​​​without leading zeros,
# return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.

import pytest


class Solution:
    def checkOnesSegment(self, s: str) -> bool:

        i = 0
        while i < len(s) and s[i] != "0":
            i += 1
        while i < len(s):
            if s[i] == "1":
                return False
            i += 1
        return True


@pytest.mark.parametrize(
    ("s", "result"),
    [("1001", False), ("11000", True), ("10000", True), ("11001", False)],
)
def test_basic(s: str, result: bool) -> None:
    assert result == Solution().checkOnesSegment(s)
