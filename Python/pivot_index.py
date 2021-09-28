# https://leetcode.com/problems/find-pivot-index/
# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index
# is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0
# because there are no elements to the left. This also applies to the right edge of the array.
# Return the leftmost pivot index. If no such index exists, return -1.

import pytest


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum = 0
        right_sum = 0
        for i in nums:
            right_sum += i
        for i, val in enumerate(nums):
            right_sum = right_sum - val
            if left_sum == right_sum:
                return i
            left_sum += val
        return -1


@pytest.mark.parametrize(
    ("nums", "result"),
    [([1, 7, 3, 6, 5, 6], 3), ([1, 2, 3], -1), ([2, 1, -1], 0), ([-1, 1], -1)],
)
def test_basic(nums: list[int], result: int) -> None:
    assert result == Solution().pivotIndex(nums)


print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))
