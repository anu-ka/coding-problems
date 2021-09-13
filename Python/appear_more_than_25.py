# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
# Given an integer array sorted in non-decreasing order,
# there is exactly one integer in the array that occurs more than 25% of the time, return that integer.
import pytest


class Solution:
    def findSpecialInteger1(self, arr: list[int]) -> int:
        num = arr[0]
        min_freq = len(arr) * 0.25
        i = 0
        dict_freq = {}
        for i in arr:
            try:
                dict_freq[i] += 1
            except KeyError:
                dict_freq[i] = 1
        for i in dict_freq:
            if dict_freq[i] > min_freq:
                return i
        return num


@pytest.mark.parametrize(
    ("arr", "result"), [([1, 2, 2, 6, 6, 6, 6, 7, 10], 6), ([1, 1], 1)]
)
def test_basic(arr: list[int], result: int) -> None:
    assert result == Solution().findSpecialInteger(arr)
