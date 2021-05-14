# https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

# You are given an array rectangles where rectangles[i] = [li, wi] represents the ith rectangle of length li and width wi.

# You can cut the ith rectangle to form a square with a side length of k if both k <= li and k <= wi.

# For example, if you have a rectangle [4,6], you can cut it to get a square with a side length of at most 4.

# Let maxLen be the side length of the largest square you can obtain from any of the given rectangles.

# Return the number of rectangles that can make a square with a side length of maxLen.


import pytest


class Solution:
    def countGoodRectangles(self, rectangles: list[list[int]]) -> int:

        count = {0: 0}
        max_side = 0
        for l, w in rectangles:
            val = l if l < w else w
            max_side = val if val > max_side else max_side
            try:
                count[val] += 1
            except KeyError:
                count[val] = 1
        return count[max_side]


@pytest.mark.parametrize(
    ("rectangles", "expected"),
    [([[5, 8], [3, 9], [5, 12], [16, 5]], 3), ([[2, 3], [3, 7], [4, 3], [3, 7]], 3)],
)
def test_basic(rectangles: list[list[int]], expected: int):
    assert expected == Solution().countGoodRectangles(rectangles)
