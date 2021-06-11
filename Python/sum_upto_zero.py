# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
# Given an integer n, return any array containing n unique integers such that they add up to 0.

import pytest


class Solution:
    def sumZero(self, n: int) -> list[int]:
        if n == 1:
            return [0]
        mid = n // 2
        result = []
        i = 1
        while i <= mid:
            result.append(i)
            result.append(-i)
            i += 1
        if n % 2 != 0:
            result.append(0)
        return result


@pytest.mark.parametrize(
    ("n", "expected"), [(1, [0]), (2, [1, -1]), (3, [1, -1, 0]), (4, [1, -1, 2, -2])]
)
def test_basic(n: int, expected: list[int]) -> None:
    assert expected == Solution().sumZero(n)
