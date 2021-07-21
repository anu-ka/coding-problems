# Given a non-empty array of non-negative integers nums,
# the degree of this array is defined as the maximum frequency of any one of its elements.
# Your task is to find the smallest possible length of a (contiguous) subarray of nums,
# that has the same degree as nums.

import pytest


class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        degree = len(nums)
        repeated_nums = []
        temp_dict = {}
        count = 0

        for i in nums:
            try:
                temp_dict[i] += 1
            except KeyError:
                temp_dict[i] = 1
            if count < temp_dict[i]:
                count = temp_dict[i]

        for i in temp_dict:
            if temp_dict[i] == count:
                repeated_nums.append(i)
        start = 0
        for n in repeated_nums:
            i = 0
            while i < len(nums):
                if nums[i] == n:
                    start = i
                    break
                i += 1
            i = len(nums) - 1
            while i >= 0:
                if nums[i] == n:
                    end = i
                    break
                i -= 1
            if degree > (end - start + 1):
                degree = end - start + 1
        return degree


@pytest.mark.parametrize(
    ("nums", "expected"),
    [([1, 2, 2, 3, 1], 2), ([1, 2, 2, 3, 1, 4, 2], 6), ([2, 1], 1)],
)
def test_basic(nums: list[int], expected: int):
    assert expected == Solution().findShortestSubArray(nums)
