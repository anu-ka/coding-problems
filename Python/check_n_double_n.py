# https://leetcode.com/problems/check-if-n-and-its-double-exist/
# Given an array arr of integers, check if there exists two integers N and M such that
# N is the double of M ( i.e. N = 2 * M).
# More formally check if there exists two indices i and j such that :

# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]


import pytest


class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        array_double = {}
        for i in arr:
            try:
                array_double[i] += 1
            except KeyError:
                array_double[i] = 1
        for i in arr:
            if i == 0:
                if array_double[i] == 2:
                    return True
            elif (i + i) in array_double:
                return True

        return False


@pytest.mark.parametrize(
    ("arr", "result"),
    [
        ([10, 2, 5, 3], True),
        ([-2, 0, 10, -19, 4, 6, -8], False),
        ([-2, 4, 0, 1], False),
        ([-2, 4, 0, 1, 0], True),
        ([0, 0], True),
    ],
)
def test_basic(arr: list[int], result: bool) -> None:
    assert result == Solution().checkIfExist(arr)
