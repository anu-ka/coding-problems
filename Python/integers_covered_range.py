# https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/
import pytest


class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        dict_nums = {i: 0 for i in range(left, right + 1)}

        for (i, j) in ranges:
            while i <= j:
                dict_nums[i] = 1
                i += 1

        return all(dict_nums.values())


@pytest.mark.parametrize(
    ("ranges", "left", "right", "result"),
    [
        ([[1, 2], [3, 4], [5, 6]], 2, 5, True),
        ([[1, 50]], 1, 50, True),
        ([[1, 2], [5, 6]], 2, 5, False),
    ],
)
def test_isCovered(
    ranges: list[list[int]], left: int, right: int, result: bool
) -> None:
    assert result == Solution().isCovered(ranges, left, right)


print(Solution().isCovered([[1, 2], [3, 4], [5, 6]], 2, 5))
