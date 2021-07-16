# https://leetcode.com/problems/set-mismatch/
# You have a set of integers s, which originally contains all the numbers from 1 to n.
# Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set,
# which results in repetition of one number and loss of another number.
# You are given an integer array nums representing the data status of this set after the error.
# Find the number that occurs twice and the number that is missing and return them in the form of an array.
import pytest


class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        ref_dict = {}
        repeated = 0
        existing_sum = 0
        for i in nums:
            existing_sum += i
            try:
                ref_dict[i] += 1
                repeated = i
            except KeyError:
                ref_dict[i] = 1
        n = len(nums)
        sum = n * (n + 1) // 2
        existing_sum = existing_sum - repeated
        missing = sum - existing_sum
        return [repeated, missing]


@pytest.mark.parametrize(
    ("nums", "result"), [([1, 2, 2, 4], [2, 3]), ([2, 2], [2, 1]), ([1, 1], [1, 2])]
)
def test_basic(nums: list[int], result: list[int]) -> None:
    assert result == Solution().findErrorNums(nums)
