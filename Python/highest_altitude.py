# https://leetcode.com/problems/find-the-highest-altitude/submissions/
# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes.
# The biker starts his trip on point 0 with altitude equal 0.
# You are given an integer array gain of length n where
# gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n).
# Return the highest altitude of a point.

import pytest


class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        start = 0
        highest = 0
        for i in gain:
            start = start + i
            if start > highest:
                highest = start
        return highest


@pytest.mark.parametrize(
    ("gain", "expected"), [([-5, 1, 5, 0, -7], 1), ([-4, -3, -2, -1, 4, 3, 2], 0)]
)
def test_basic(gain: list[int], expected: int):
    assert expected == Solution().largestAltitude(gain)
