# https://leetcode.com/problems/container-with-most-water/
import pytest


class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0
        j = len(height) - 1
        max_area = 0
        while i < j:
            area = (j - i) * min(height[i], height[j])
            if max_area < area:
                max_area = area
            if height[i] <= height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
        return max_area


@pytest.mark.parametrize(("height", "result"), [([1, 8, 6, 2, 5, 4, 8, 3, 7], 49)])
def test_maxarea(height: list[int], result: int) -> None:
    assert result == Solution().maxArea(height)
