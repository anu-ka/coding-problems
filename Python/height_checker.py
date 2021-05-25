# https://leetcode.com/problems/height-checker/
# A school is trying to take an annual photo of all the students.
# The students are asked to stand in a single file line in non-decreasing order by height.
# Let this ordering be represented by the integer array expected
# where expected[i] is the expected height of the ith student in line.
# You are given an integer array heights representing the current order that the students are standing in.
# Each heights[i] is the height of the ith student in line (0-indexed).
# Return the number of indices where heights[i] != expected[i].

import pytest


class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        count = 0
        # find the lowest and highest heights
        high = heights[0]
        low = heights[0]
        result_height = []
        for i in heights:
            if i > high:
                high = i
            if i < low:
                low = i
        # build a dictionary from low to high
        dict_vals = {}
        for i in range(low, high + 1):
            dict_vals[i] = 0
        for i in heights:
            dict_vals[i] += 1
        for i in dict_vals:
            while dict_vals[i] > 0:
                result_height.append(i)
                dict_vals[i] -= 1

        i = 0
        while i < len(heights):
            if heights[i] - result_height[i] != 0:
                count += 1
            i += 1
        return count


@pytest.mark.parametrize(
    ("heights", "expected"),
    [
        ([1, 1, 4, 2, 1, 3], 3),
        ([5, 1, 2, 3, 4], 5),
        ([1, 2, 3, 4, 5], 0),
    ],
)
def test_basic(heights: list[int], expected: int):
    assert expected == Solution().heightChecker(heights)
