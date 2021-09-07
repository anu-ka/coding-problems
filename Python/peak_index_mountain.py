# https://leetcode.com/problems/peak-index-in-a-mountain-array/
# Let's call an array arr a mountain if the following properties hold:
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... arr[i-1] < arr[i]
# arr[i] > arr[i+1] > ... > arr[arr.length - 1]
# Given an integer array arr that is guaranteed to be a mountain,
# return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

import pytest


class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:

        i = 1
        while i < len(arr) - 1:
            if arr[i] - arr[i - 1] > 0 and arr[i] - arr[i + 1] > 0:
                return i
            i += 1
        return -1


@pytest.mark.parametrize(
    ("arr", "result"),
    [
        ([0, 1, 0], 1),
        ([0, 2, 1, 0], 1),
        ([3, 4, 5, 1], 2),
        ([24, 69, 100, 99, 79, 78, 67, 36, 26, 19], 2),
    ],
)
def test_basic(arr: list[int], result: int) -> None:
    assert result == Solution().peakIndexInMountainArray(arr)
