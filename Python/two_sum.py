# https://leetcode.com/problems/two-sum/
import pytest


class TwoSum(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, val_i in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if val_i + nums[j] == target:
                    return [i, j]
        return []


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [([1, 2, 2, 5], 4, [1, 2]), ([1, 2, 3, 4], 7, [2, 3])],
)
def test_basic(nums: list, target: int, expected: list):
    assert expected == TwoSum().twoSum(nums, target)
