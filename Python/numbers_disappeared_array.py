# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
import pytest


class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        temp_dict = {i: -1 for i in range(1, len(nums) + 1)}
        result = []

        for i in nums:
            if i in temp_dict:
                temp_dict[i] = i

        for i in temp_dict:
            if temp_dict[i] == -1:
                result.append(i)
        return result


@pytest.mark.parametrize(
    ("nums", "result"), [([4, 3, 2, 7, 8, 2, 3, 1], [5, 6]), ([1, 1, 1], [2, 3])]
)
def test_findDisappearedNumbers(nums: list[int], result: list[int]) -> None:
    assert result == Solution().findDisappearedNumbers(nums)
