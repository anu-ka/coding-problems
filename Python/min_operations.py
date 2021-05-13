# https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/
# Return the minimum number of operations needed to make nums strictly increasing.
# An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1.
# An array of length 1 is trivially strictly increasing.

import pytest


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        i = 0
        count = 0
        while i + 1 < len(nums):
            if nums[i + 1] <= nums[i]:
                diff = (nums[i] - nums[i + 1]) + 1
                nums[i + 1] += diff
                count += diff
            i += 1
        return count


@pytest.mark.parametrize(
    ("nums", "expected"), [([1, 1, 1], 3), ([1, 2, 3], 0), ([1, 5, 2, 3], 8)]
)
def test_basic(nums: list[int], expected: int):
    assert expected == Solution().minOperations(nums)
