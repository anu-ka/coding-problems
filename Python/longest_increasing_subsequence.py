# https://leetcode.com/problems/longest-continuous-increasing-subsequence/
# Given an unsorted array of integers nums, return the length of the longest continuous increasing
# subsequence (i.e. subarray). The subsequence must be strictly increasing.
# A continuous increasing subsequence is defined by two indices l and r (l < r) such that
# it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].

import pytest


class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        longest = 1
        i = 0
        temp_length = 1
        while i + 1 < len(nums):
            if nums[i + 1] > nums[i]:
                temp_length += 1
                if longest < temp_length:
                    longest = temp_length
            else:
                temp_length = 1
            i += 1

        return longest


@pytest.mark.parametrize(("nums", "longest"), [([1, 3, 5, 4, 7], 3), ([2, 2, 2, 2], 1)])
def test_basic(nums: list[int], longest: int) -> None:
    assert longest == Solution().findLengthOfLCIS(nums)
