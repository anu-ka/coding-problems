# https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/
# Given an integer n, return a string with n characters such that
# each character in such string occurs an odd number of times.
# The returned string must contain only lowercase English letters.
# If there are multiples valid strings, return any of them.

import pytest


class Solution:
    def generateTheString(self, n: int) -> str:
        result = " "
        if n % 2 == 0:
            result = "a" * (n - 1)
            result += "b"
        else:
            result = "a" * n

        return result


@pytest.mark.parametrize(("n", "expected"), [(2, "ab"), (3, "aaa")])
def test_basic(n: int, expected: str):
    assert expected == Solution().generateTheString(n)
