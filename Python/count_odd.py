# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
# Given two non-negative integers low and high.
# Return the count of odd numbers between low and high (inclusive).
import pytest


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = 0
        total = high - low + 1
        count = total // 2
        if low % 2 != 0 and high % 2 != 0:
            count += 1

        return count


@pytest.mark.parametrize(("low", "high", "result"), [(1, 5, 3), (2, 4, 1), (1, 6, 3)])
def test_countOdds(low: int, high: int, result: int) -> None:
    assert result == Solution().countOdds(low, high)
