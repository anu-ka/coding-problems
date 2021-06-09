# https://leetcode.com/problems/missing-number/
# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.

import pytest


class Solution:
    def missingNumber(self, nums: list) -> int:
        highest = 0
        for i in nums:
            if i > highest:
                highest = i
        sum = (highest * (highest + 1)) // 2
        hasZero = False
        for i in nums:
            if i == 0:
                hasZero = True
            sum -= i
        if hasZero and sum == 0:
            return highest + 1
        return sum


@pytest.mark.parametrize(
    ("nums", "sum"),
    [([3, 0, 1], 2), ([0, 1], 2), ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8), ([0], 1)],
)
def test_basic(nums: list[int], sum: int) -> None:
    assert sum == Solution().missingNumber(nums)
