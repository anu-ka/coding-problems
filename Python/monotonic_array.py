# https://leetcode.com/problems/monotonic-array/
# An array is monotonic if it is either monotone increasing or monotone decreasing.
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
# An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
# Given an integer array nums, return true if the given array is monotonic, or false otherwise.

from _pytest.recwarn import T
import pytest


class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        increasing = False
        decreasing = False

        i = 0
        while i < len(nums) - 1:
            if nums[i + 1] > nums[i]:
                increasing = True
            elif nums[i + 1] == nums[i]:
                pass
            else:
                decreasing = True
            if increasing and decreasing:
                return False
            i += 1
        return True


@pytest.mark.parametrize(
    ("nums", "result"),
    [([1, 2, 3], True), ([1, 2, 2, 3], True), ([3, 2, 2, 1], True), ([3, 2, 5], False)],
)
def test_ismonotonic(nums: list[int], result: bool) -> None:
    assert result == Solution().isMonotonic(nums)
