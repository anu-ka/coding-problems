# https://leetcode.com/problems/two-sum/
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
import pytest


class TwoSum(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, val_i in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if val_i + nums[j] == target:
                    return [i, j]
        return []

    def twoSum_with_O_N(self, nums: list[int], target: int) -> list[int]:
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


print(TwoSum().twoSum_with_O_N([1, 2, 2, 5], 4))
print(TwoSum().twoSum_with_O_N([3, 3], 6))
print(TwoSum().twoSum_with_O_N([2, 7, 11, 15], 9))
print(TwoSum().twoSum_with_O_N([3, 2, 4], 6))


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [([1, 2, 2, 5], 4, [1, 2]), ([1, 2, 3, 4], 7, [2, 3])],
)
def test_basic(nums: list, target: int, expected: list):
    assert expected == TwoSum().twoSum(nums, target)
