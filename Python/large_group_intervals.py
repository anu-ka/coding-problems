# https://leetcode.com/problems/positions-of-large-groups/
# In a string s of lowercase letters, these letters form consecutive groups of the same character.
# For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".
# A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive) of the group. In the above example, "xxxx" has the interval [3,6].
# A group is considered large if it has 3 or more characters.
# Return the intervals of every large group sorted in increasing order by start index.

import pytest


class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        i = 0
        j = 0
        result = []
        while i < len(s):
            index = []
            j = i + 1
            while j < len(s) and s[i] == s[j]:
                j += 1
            if j - 1 - i >= 2:
                index.append(i)
                index.append(j - 1)
                result.append(index)
            i = j
        return result


@pytest.mark.parametrize(
    ("s", "result"),
    [
        ("abbxxxxzzy", [[3, 6]]),
        ("aabbbccccee", [[2, 4], [5, 8]]),
        ("abc", []),
        ("abcdddeeeeaabbbcd", [[3, 5], [6, 9], [12, 14]]),
    ],
)
def test_basic(s: str, result: list[list[int]]) -> None:
    assert result == Solution().largeGroupPositions(s)
