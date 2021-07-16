# https://leetcode.com/problems/maximum-product-of-three-numbers/
# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

import pytest


class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        high1 = nums[0]
        high2 = nums[1]
        high3 = nums[2]
        sum = high1 + high2 + high3

        for i in nums[0:3]:
            if i < high1:
                high1 = i
            if i > high3:
                high3 = i

        high2 = sum - (high1 + high3)
        low1 = high1
        low2 = high2
        for n in nums[3:]:
            if n >= high3:
                high1 = high2
                high2 = high3
                high3 = n
            elif n < high3 and n <= high2 and n > high1:
                high1 = n
            elif n < high3 and n >= high2:
                high1 = high2
                high2 = n

            if n < low2 and n > low1:
                low2 = n
            elif n <= low2 and n <= low1:
                low2 = low1
                low1 = n

        return max(high1 * high2 * high3, low1 * low2 * high3)


@pytest.mark.parametrize(
    ("nums", "result"),
    [
        ([1, 2, 3], 6),
        ([-1, -2, -3, -4], -6),
        ([-1, 2, 3, 4, -100, -98], 39200),
        ([-1, -2, 1], 2),
        ([1, 2, 3, 2], 12),
        ([1, 1, 2, 2], 4),
    ],
)
def test_basic(nums: list[int], result: int) -> None:
    assert result == Solution().maximumProduct(nums)
