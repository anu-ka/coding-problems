# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/639/week-4-september-22nd-september-28th/3990/
# Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
# Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
# Return any answer array that satisfies this condition.

import pytest


class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        odd = []
        even = []
        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        i = 0
        result = []
        while i < len(even):
            result.append(even[i])
            result.append(odd[i])
            i += 1

        return result

    def sortArrayByParityII_InPlace(self, nums: list[int]) -> list[int]:
        i = 0
        j = i + 1
        while i < len(nums):
            if j < i + 1:
                j = i + 1
            if i % 2 == 0 and nums[i] % 2 != 0:
                while j < len(nums):
                    if nums[j] % 2 == 0:
                        temp = nums[j]
                        nums[j] = nums[i]
                        nums[i] = temp
                        i += 1
                        break
                    j += 2
            elif i % 2 != 0 and nums[i] % 2 == 0:
                j = i + 1
                while j < len(nums):
                    if nums[j] % 2 != 0:
                        temp = nums[j]
                        nums[j] = nums[i]
                        nums[i] = temp
                        i += 1
                        break
                    j += 2
            i += 1
        return nums


@pytest.mark.parametrize(
    ("nums", "result"),
    [
        ([4, 2, 5, 7], [4, 5, 2, 7]),
        ([2, 3], [2, 3]),
        ([2, 4, 6, 8, 1, 3, 5, 7], [2, 1, 4, 3, 6, 5, 8, 7]),
    ],
)
def test_basic(nums: list[int], result: list[int]) -> None:
    assert result == Solution().sortArrayByParityII(nums)


@pytest.mark.parametrize(
    ("nums", "result"),
    [
        ([4, 2, 5, 7], [4, 5, 2, 7]),
        ([2, 3], [2, 3]),
        ([2, 4, 6, 8, 1, 3, 5, 7], [2, 1, 6, 5, 4, 3, 8, 7]),
    ],
)
def test_basic2(nums: list[int], result: list[int]) -> None:
    assert result == Solution().sortArrayByParityII_InPlace(nums)
