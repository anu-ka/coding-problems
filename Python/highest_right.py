# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
# Given an array arr, replace every element in that array with the greatest element among the elements to its right,
# and replace the last element with -1.
# After doing so, return the array.

import pytest


class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        result = [-1] * len(arr)
        last = len(arr) - 1
        high = arr[last]
        while last >= 1:
            j = last - 1
            result[j] = high
            if arr[j] > high:
                high = arr[j]
            last -= 1
        return result


@pytest.mark.parametrize(
    ("arr", "expected"), [([17, 18, 5, 4, 6, 1], [18, 6, 6, 6, 1, -1]), ([400], [-1])]
)
def test_basic(arr: list[int], expected: list[int]) -> None:
    assert expected == Solution().replaceElements(arr)
