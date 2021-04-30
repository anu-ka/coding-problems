# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

import pytest


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        if len(nums) == 0:
            return []
        result = []
        result.append(nums[0])
        j = 0
        i = 1
        while i < len(nums):
            result.append(nums[i] + result[j])
            i = i + 1
            j = j + 1
        return result


@pytest.mark.parametrize(
    ("nums", "expected"), [([1, 1, 1, 1], [1, 2, 3, 4]), ([1, 2, 3, 4], [1, 3, 6, 10])]
)
def test_basic(nums: list[int], expected: list[int]):
    result = Solution().runningSum(nums)
    assert len(expected) == len(result)
    assert expected == result
