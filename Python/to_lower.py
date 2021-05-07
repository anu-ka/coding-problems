# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
# https://leetcode.com/problems/to-lower-case/


import pytest


class Solution:
    def toLowerCase(self, str: str) -> str:
        lower = ""
        for i in str:
            ordVal = ord(i)
            if ordVal >= 65 and ordVal <= 90:
                lower += chr(ordVal + 32)
            else:
                lower += i
        return lower


@pytest.mark.parametrize(
    ("str", "expected"), [("aAbB", "aabb"), ("aabb", "aabb"), ("a1@B", "a1@b")]
)
def test_basic(str: str, expected: str):
    assert expected == Solution().toLowerCase(str)
