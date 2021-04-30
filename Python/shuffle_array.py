# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].
# https://leetcode.com/problems/shuffle-the-array/

import pytest


class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        result = []
        array1 = nums[0:n]
        array2 = nums[n : len(nums)]
        for i in range(0, n):
            result.append(array1[i])
            result.append(array2[i])
        return result


@pytest.mark.parametrize(
    ("nums", "n", "expected"),
    [
        ([1, 2, 3, 4, 5, 6], 3, [1, 4, 2, 5, 3, 6]),
        ([4, 5, 11, 12], 2, [4, 11, 5, 12]),
    ],
)
def test_basic(nums: list[int], n: int, expected: list[int]):
    result = Solution().shuffle(nums, n)
    assert len(expected) == len(result)
    assert expected == result
