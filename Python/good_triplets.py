# https://leetcode.com/problems/count-good-triplets/submissions/
# Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.
# A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
# 0 <= i < j < k < arr.length
# |arr[i] - arr[j]| <= a
# |arr[j] - arr[k]| <= b
# |arr[i] - arr[k]| <= c
# Where |x| denotes the absolute value of x.
# Return the number of good triplets.

import pytest


class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        count = 0
        i = 0
        while i < len(arr):
            j = i + 1
            while j < len(arr):
                k = j + 1
                if abs(arr[i] - arr[j]) <= a:
                    while k < len(arr):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            count += 1
                        k += 1
                j += 1
            i += 1

        return count


@pytest.mark.parametrize(
    ("arr", "a", "b", "c", "expected"),
    [([3, 0, 1, 1, 9, 7], 7, 2, 3, 4), ([1, 1, 2, 2, 3], 0, 0, 1, 0)],
)
def test_basic(arr: list[int], a: int, b: int, c: int, expected: int):
    assert expected == Solution().countGoodTriplets(arr, a, b, c)
