# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
# Given the array of integers nums, you will choose two different indices i and j of that array.
# Return the maximum value of (nums[i]-1)*(nums[j]-1).
import pytest


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # form the array and find biggest num
        large1 = 0
        tempArr = []
        index = -1
        for val in nums:
            val -= 1
            if val > 0:
                tempArr.append(val)
        # find largest number
        for i, val in enumerate(tempArr):
            if val > large1:
                large1 = val
                index = i

        # find 2nd biggest num
        large2 = 0
        for i, val in enumerate(tempArr):
            if val > large2 and val <= large1 and i != index:
                large2 = val
        return large1 * large2


@pytest.mark.parametrize(("nums", "expected"), [([3, 4, 5, 2], 12), ([1, 5, 4, 5], 16)])
def test_basic(nums: list[int], expected: int):
    assert expected == Solution().maxProduct(nums)
