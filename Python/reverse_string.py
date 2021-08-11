# https://leetcode.com/problems/reverse-string-ii/
# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
# If there are fewer than k characters left, reverse all of them.
#  If there are less than 2k but greater than or equal to k characters,
# then reverse the first k characters and left the other as original.
import pytest


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        rev = ""
        i = 0
        j = 0
        n = k
        stop = n * 2
        while i <= len(s):
            temp = s[i:n]
            r = temp[::-1]
            l = s[n:stop]
            rev += r + l
            i = stop
            n = stop + k
            stop += k * 2
        return rev


@pytest.mark.parametrize(
    ("s", "k", "result"),
    [
        ("abcde", 1, "abcde"),
        ("abcde", 2, "bacde"),
        ("abcdefg", 2, "bacdfeg"),
        ("abc", 4, "cba"),
    ],
)
def test_basic(s: str, k: int, result: str) -> None:
    assert result == Solution().reverseStr(s, k)
