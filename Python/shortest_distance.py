# https://leetcode.com/problems/shortest-distance-to-a-character/
# Given a string s and a character c that occurs in s,
# return an array of integers answer where answer.length == s.length and
# answer[i] is the distance from index i to the closest occurrence of character c in s.
# The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

import pytest


class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        positions = []
        for index, val in enumerate(s):
            if val == c:
                positions.append(index)
        distance_char = []
        for i in range(0, len(s)):
            temp = len(s)
            for index in positions:
                if abs(i - index) < temp:
                    temp = abs(i - index)
                    if temp == 0:
                        break
            distance_char.append(temp)

        return distance_char


@pytest.mark.parametrize(
    ("s", "c", "expected"),
    [
        ("loveleetcode", "e", [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]),
        ("aaab", "b", [3, 2, 1, 0]),
    ],
)
def test_basic(s: str, c: str, expected: list[int]):
    assert expected == Solution().shortestToChar(s, c)
