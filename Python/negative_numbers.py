# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise,
# return the number of negative numbers in grid.
import pytest


class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        count = 0
        for row in grid:
            if row[-1] >= 0:
                continue
            if row[0] < 0:
                count += len(row)
                continue
            i = 0
            while i < len(row):
                if row[i] < 0:
                    count += len(row) - i
                    break
                i += 1
        return count


@pytest.mark.parametrize(
    ("grid", "expected"),
    [
        ([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]], 8),
        ([[3, 2], [1, 0]], 0),
    ],
)
def test_basic(grid: list[list[int]], expected: int):
    assert expected == Solution().countNegatives(grid)
