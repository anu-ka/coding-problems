# https://leetcode.com/problems/kth-missing-positive-number/
import pytest


class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        first = arr[0]
        result = []
        i = 1
        l = 0
        while l < len(arr):
            first = arr[l]
            while i < first:
                result.append(i)
                i += 1
            i = first + 1
            l += 1

        if len(result) < k:
            i = arr[len(arr) - 1] + 1
            p = k
            while p >= 0:
                result.append(i)
                i += 1
                p -= 1

        return result[k - 1]


@pytest.mark.parametrize(
    ("arr", "k", "result"), [([2, 3, 4, 7, 11], 5, 9), ([1, 2, 3, 4], 2, 6)]
)
def test_missingpositive(arr: list[int], k: int, result: int) -> None:
    assert result == Solution().findKthPositive(arr, k)
