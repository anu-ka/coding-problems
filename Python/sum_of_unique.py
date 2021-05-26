# https://leetcode.com/problems/sum-of-unique-elements/
# You are given an integer array nums.
# The unique elements of an array are the elements that appear exactly once in the array.
# Return the sum of all the unique elements of nums.

import pytest


class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        check_dict = {}
        sum = 0
        for i in nums:
            try:
                check_dict[i] += 1
            except KeyError:
                check_dict[i] = 1

        for i in check_dict:
            if check_dict[i] == 1:
                sum += i
        return sum


@pytest.mark.parametrize(
    ("nums", "expected"),
    [([1, 1, 1, 1, 1], 0), ([1, 1, 2, 3], 5), ([1, 2, 3, 4, 5], 15)],
)
def test_basic(nums: list[int], expected: int):
    assert expected == Solution().sumOfUnique(nums)
