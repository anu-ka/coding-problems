from __future__ import division
from collections import defaultdict

import pytest


class mergesort:
    def merge_sort(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums

        if len(nums) == 2:
            return [nums[0], nums[1]] if nums[0] < nums[1] else [nums[1], nums[0]]

        mid = len(nums) // 2
        return self.merge(self.merge_sort(nums[0:mid]), self.merge_sort(nums[mid:]))

    def merge(self, left: list[int], right: list[int]) -> list[int]:
        result = []
        while len(left) > 0 and len(right) > 0:
            result.append(left.pop(0) if left[0] < right[0] else right.pop(0))

        if len(left) > 0:
            result += left

        if len(right) > 0:
            result += right

        return result


nums = [1, 3, 5, 2, 4, 6]


@pytest.mark.parametrize(
    ("nums", "result"), [([1, 3, 5, 2, 4, 6], [1, 2, 3, 4, 5, 6]), ([], [])]
)
def test_mergesort(nums: list[int], result: list[int]) -> None:
    assert result == mergesort().merge_sort(nums)
