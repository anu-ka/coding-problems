# https://leetcode.com/problems/largest-number-at-least-twice-of-others/
# You are given an integer array nums where the largest integer is unique.
# Determine whether the largest element in the array is at least twice as much as every other number in the array.
# If it is, return the index of the largest element, or return -1 otherwise.
import pytest


class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        # find the highest and a number lesser than highest
        highest = nums[0]
        less_high = nums[1]
        index = 0
        for i, val in enumerate(nums):
            if val > highest:
                less_high = highest
                highest = val
                index = i
            elif val > less_high and val < highest:
                less_high = val
        if highest >= less_high * 2:
            return index
        return -1


@pytest.mark.parametrize(
    ("nums", "index"),
    [
        ([1, 2, 3, 4], -1),
        ([1, 1, 2, 8], 3),
        ([3, 6, 1, 0], 1),
        ([1], 0),
        ([100, 20], 0),
        ([0, 0, 3, 2], -1),
    ],
)
def test_basic(nums: list[int], index: int) -> None:
    assert index == Solution().dominantIndex(nums)
