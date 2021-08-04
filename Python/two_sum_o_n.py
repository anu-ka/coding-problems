# https://leetcode.com/problems/two-sum/
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
import pytest


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []
        dict_nums = {}
        dict_index = {}
        num = nums[0]
        for i, val in enumerate(nums):
            try:
                dict_nums[val] += 1
                dict_index[val].append(i)
            except KeyError:
                dict_nums[val] = 1
                dict_index[val] = [i]

        for i in dict_nums:
            if target - i == i:
                if dict_nums[i] == 2:
                    num = i
                    return dict_index[num]
                else:
                    continue

            if target - i in dict_nums:
                num = i
                num2 = target - num
                return [dict_index[num][0], dict_index[num2][0]]
        return result


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [
        ([1, 2, 2, 5], 4, [1, 2]),
        ([1, 2, 3, 4], 7, [2, 3]),
        ([3, 3], 6, [0, 1]),
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
    ],
)
def test_basic(nums: list, target: int, expected: list):
    assert expected == Solution().twoSum(nums, target)
