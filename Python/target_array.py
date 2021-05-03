# Given two arrays of integers nums and index. Your task is to create target array under the following rules:
# Initially target array is empty.
# From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
# Repeat the previous step until there are no elements to read in nums and index.
# Return the target array.
# It is guaranteed that the insertion operations will be valid.
# Input: nums = [0,1,2,3,4], index = [0,1,2,2,1] ,Output: [0,4,1,3,2]
# https://leetcode.com/problems/create-target-array-in-the-given-order/
import pytest


class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        result = []
        j = 0
        for i in nums:
            result.insert(index[j], i)
            j += 1
        return result


@pytest.mark.parametrize(
    ("nums", "index", "expected"),
    [([0, 1, 2, 3, 4], [0, 1, 2, 2, 1], [0, 4, 1, 3, 2]), ([1], [0], [1])],
)
def test_basic(nums, index, expected):
    assert expected == Solution().createTargetArray(nums, index)
