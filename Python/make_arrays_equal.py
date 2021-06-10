# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/
# Given two integer arrays of equal length target and arr.
# In one step, you can select any non-empty sub-array of arr and reverse it.
# You are allowed to make any number of steps.
# Return True if you can make arr equal to target, or False otherwise.

import pytest


class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        input_dict = {}
        for i in target:
            try:
                input_dict[i] += 1
            except KeyError:
                input_dict[i] = 1
        arr_dict = {}
        for i in arr:
            try:
                arr_dict[i] += 1
            except KeyError:
                arr_dict[i] = 1
        for i in input_dict:
            if i not in arr_dict:
                return False
            if input_dict[i] != arr_dict[i]:
                return False
        return True


@pytest.mark.parametrize(
    ("target", "arr", "expected"),
    [
        ([1, 2, 3, 4], [2, 4, 1, 3], True),
        ([7], [7], True),
        ([3, 7, 9], [3, 7, 11], False),
        ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1], True),
    ],
)
def test_basic(target: list[int], arr: list[int], expected: bool) -> None:
    assert expected == Solution().canBeEqual(target, arr)
