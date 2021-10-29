# https://leetcode.com/problems/last-stone-weight/
# You are given an array of integers stones where stones[i] is the weight of the ith stone.
# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together.
# Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.
# Return the smallest possible weight of the left stone. If there are no stones left, return 0.

import pytest


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        ref_stones = stones
        i = 0
        ones = 0
        while i < len(ref_stones):
            first = ref_stones[0]
            if len(ref_stones) > 1:
                second = ref_stones[1]
            else:
                second = ones
                break
            if first < second:
                temp = first
                first = second
                second = temp
            i = 2
            new_list = []
            while i < len(ref_stones):
                if ref_stones[i] == 1:
                    ones += 1
                elif ref_stones[i] >= first and ref_stones[i] > second:
                    new_list.append(second)
                    second = first
                    first = ref_stones[i]
                elif ref_stones[i] >= second and ref_stones[i] < first:
                    new_list.append(second)
                    second = ref_stones[i]
                else:
                    new_list.append(ref_stones[i])
                i += 1
            i = 0
            diff = first - second
            if diff == 1:
                ones += 1
            elif diff > 0:
                new_list.append(diff)
            if len(new_list) == 0:
                return ones % 2
            ref_stones = new_list

        if second > first:
            second = second - first
            return second % 2

        return abs(first - second)


@pytest.mark.parametrize(
    ("stones", "result"),
    [
        ([2, 7, 4, 1, 8, 1], 1),
        ([9, 3, 2, 10], 0),
        ([4, 3, 4, 3, 2], 2),
        ([7, 5, 6, 9, 10, 5], 0),
        ([3, 4, 8, 9, 4, 2, 5, 7, 10], 0),
    ],
)
def test_lastStoneWeight(stones: list[int], result: int) -> None:
    assert Solution().lastStoneWeight(stones) == result
