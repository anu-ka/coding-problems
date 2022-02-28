# https://leetcode.com/problems/binary-search/
import pytest


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        index = -1
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            if start == end:
                if target != nums[mid]:
                    return -1

            if target < nums[mid]:
                end = mid
            elif target > nums[mid]:
                start = mid + 1

        return index


@pytest.mark.parametrize(
    ("nums", "target", "index"),
    [([-1, 0, 3, 5, 9, 12], 2, -1), ([5], 5, 0), ([-1, 0, 3, 5, 9, 12], 9, 4)],
)
def test_search(nums: list[int], target: int, index: int):
    assert index == Solution().search(nums, target)
