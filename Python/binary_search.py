# https://leetcode.com/problems/binary-search/
# Given an array of integers nums which is sorted in ascending order, and an integer target,
# write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.
# [1,2,3,4,5] ,3 -> 2
# [1,2,3,4,5,6,7,8,9,10] , 4 -> 3
# [1,2,3,4,5,6,7,8,9,10] , 9 -> 8

import pytest


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        mid = (start + end) // 2
        if target < nums[start] or target > nums[end]:
            return -1
        while start <= end:
            if nums[start] == target:
                return start
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            mid = (start + end) // 2
        return -1


@pytest.mark.parametrize(
    ("nums", "target", "result"),
    [
        ([1, 2, 3, 4, 5], 3, 2),
        ([1, 2, 3, 4, 5, 6], 3, 2),
        ([1, 2, 3, 4, 5, 6, 7], 3, 2),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 6, 5),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 8),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 0),
        ([5], -5, -1),
    ],
)
def test_basic(nums: list[int], target: int, result: int) -> None:
    assert result == Solution().search(nums, target)
