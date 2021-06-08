# https://leetcode.com/problems/can-place-flowers/submissions/
# You have a long flowerbed in which some of the plots are planted, and some are not.
# However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
# and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

import pytest


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        i = 0
        while i + 1 < len(flowerbed) and n > 0:
            if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                i += 2
                n -= 1
            elif flowerbed[i] == 0 and flowerbed[i + 1] != 0:
                i += 3
            else:
                i += 2
        if i < len(flowerbed) and flowerbed[i - 1] == 0 and flowerbed[i] == 0 and n > 0:
            flowerbed[i] = 1
            n -= 1
        print(flowerbed)
        if n == 0:
            return True
        return False


@pytest.mark.parametrize(
    ("flowerbed", "n", "expected"),
    [([1, 0, 0, 0, 1], 1, True), ([1, 0, 0, 0, 1], 2, False)],
)
def test_basic(flowerbed: list[int], n: int, expected: bool) -> None:
    assert expected == Solution().canPlaceFlowers(flowerbed, n)
