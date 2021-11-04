# https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/
# Given a binary string s, return true if the longest contiguous segment of 1's is strictly
# longer than the longest contiguous segment of 0's in s, or return false otherwise.
# For example, in s = "110100010" the longest continuous segment of 1s has length 2,
# and the longest continuous segment of 0s has length 3.
# Note that if there are no 0's, then the longest continuous segment of 0's is considered to have a length 0.
# The same applies if there is no 1's.
import pytest


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        i = 0
        zero_count = 0
        one_count = 0
        while i < len(s):
            zeros = 0
            ones = 0
            if s[i] == "0":
                while i < len(s) and s[i] == "0":
                    zeros += 1
                    i += 1
                if zero_count < zeros:
                    zero_count = zeros
            else:
                while i < len(s) and s[i] == "1":
                    ones += 1
                    i += 1
                if one_count < ones:
                    one_count = ones

        return one_count > zero_count


@pytest.mark.parametrize(
    ("s", "result"), [("1101", True), ("111000", False), ("110100010", False)]
)
def test_checkZeroOnes(s: str, result: bool) -> None:
    assert result == Solution().checkZeroOnes(s)
