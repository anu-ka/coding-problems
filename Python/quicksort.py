import pytest


class Solution:
    def quick_sort(self, nums: list[int]) -> None:
        self.exchange(nums, 0, len(nums) - 1)

    def exchange(self, nums: list[int], start: int, end: int) -> None:
        s = start
        p = end
        if s > p or s == p:
            return
        if len(nums) == 2:
            if nums[0] > nums[1]:
                temp = nums[0]
                nums[0] = nums[1]
                nums[1] = temp
            return

        while s < p:
            if nums[s] < nums[p]:
                s += 1
            if nums[s] > nums[p]:
                temp = nums[s]
                nums[s] = nums[p - 1]
                nums[p - 1] = temp

                temp = nums[p]
                nums[p] = nums[p - 1]
                nums[p - 1] = temp

                p -= 1
            if nums[s] == nums[p]:
                break

        self.exchange(nums, start, p - 1)
        self.exchange(nums, p + 1, end)


@pytest.mark.parametrize(
    ("nums", "result"), [([3, 7, 8, 5, 2, 1, 9, 5, 4], [1, 2, 3, 4, 5, 5, 7, 8, 9])]
)
def test_quicksort(nums: list[int], result: list[int]) -> None:
    Solution().quick_sort(nums)
    assert nums == result
