# https://leetcode.com/problems/unique-number-of-occurrences/
# Given an array of integers arr,
# write a function that returns true if and only if the number of occurrences of each value in the array is unique.
import pytest


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        isUnique = True
        temp_dict = {}
        for i in arr:
            try:
                temp_dict[i] += 1
            except KeyError:
                temp_dict[i] = 1
        result_dict = {}
        for i in temp_dict:
            try:
                result_dict[temp_dict[i]] += 1
                isUnique = False
                return isUnique
            except KeyError:
                result_dict[temp_dict[i]] = 1

        return isUnique


@pytest.mark.parametrize(
    ("arr", "expected"), [([1, 2, 2, 1, 1, 3], True), ([1, 2], False)]
)
def test_basic(arr: list[int], expected: bool):
    expected == Solution().uniqueOccurrences(arr)
