# https://leetcode.com/problems/add-to-array-form-of-integer/
# The array-form of an integer num is an array representing its digits in left to right order.
# For example, for num = 1321, the array form is [1,3,2,1].
# Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

import pytest


class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        result = []
        i = len(num) - 1
        rem = 0
        while k > 0 or rem > 0:
            r = k % 10
            k = k // 10
            n = num[i] if i >= 0 else 0
            sum = r + rem + n

            res = sum % 10
            rem = sum // 10
            result.insert(0, res)
            i -= 1
        while i >= 0:
            result.insert(0, num[i])
            i -= 1
        return result


@pytest.mark.parametrize(
    ("nums", "k", "result"),
    [
        ([1, 2, 3], 5, [1, 2, 8]),
        ([1, 2, 8], 5, [1, 3, 3]),
        ([2, 1, 5], 806, [1, 0, 2, 1]),
        ([9, 9], 1, [1, 0, 0]),
    ],
)
def test_basic(nums: list[int], k: int, result: list[int]) -> None:
    assert result == Solution().addToArrayForm(nums, k)
