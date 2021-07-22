# https://leetcode.com/problems/maximum-average-subarray-i/
# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
#  Any answer with a calculation error less than 10-5 will be accepted.
import pytest


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        prev_sum = 0
        j = 0
        while j < k:
            prev_sum += nums[j]
            j += 1
        prev_avg = prev_sum / k
        max_avg = prev_avg
        prev = nums[0]

        i = 0
        while i + k < len(nums):
            curr_sum = prev_sum + nums[i + k] - prev
            curr_avg = curr_sum / k
            if max_avg < curr_avg:
                max_avg = curr_avg

            prev = nums[i + 1]
            prev_sum = curr_sum
            prev_avg = curr_avg
            i += 1
        return max_avg


@pytest.mark.parametrize(
    ("nums", "k", "expected"),
    [
        ([1, 12, -5, -6, 50, 3], 4, 12.75),
        ([1, 2, 3, 4], 2, 3.5),
        ([1, 1, 2, 2], 2, 2.0),
    ],
)
def test_basic(nums: list[int], k: int, expected: float) -> None:
    assert expected == Solution().findMaxAverage(nums, k)


print(Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4))
