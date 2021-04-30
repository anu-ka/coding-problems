# Given an array of integers nums.
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
# Return the number of good pairs.
# https://leetcode.com/problems/number-of-good-pairs/

import pytest


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = 0
        for i, val_i in enumerate(nums):
            temp = nums[i + 1 :]
            for val_j in temp:
                if val_i == val_j:
                    count += 1
        return count


@pytest.mark.parametrize(
    ("pairs", "expected"), [([1, 2, 3, 1, 1, 3], 4), ([1, 1, 1, 1], 6)]
)
def test_basic(pairs: list[int], expected: int):
    assert expected == Solution().numIdenticalPairs(pairs)
