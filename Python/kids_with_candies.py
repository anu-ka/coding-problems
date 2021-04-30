# Given the array candies and the integer extraCandies,
# where candies[i] represents the number of candies that the ith kid has.
# For each kid check if there is a way to distribute extraCandies among the kids
# such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

import pytest


class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        can_have = []
        # find the highest candy
        highest = 0
        for candy in candies:
            if highest < candy:
                highest = candy

        for candy in candies:
            if candy + extraCandies >= highest:
                can_have.append(True)
            else:
                can_have.append(False)

        return can_have


@pytest.mark.parametrize(
    ("candies", "extra", "expected"),
    [
        ([2, 3, 5, 1, 3], 3, [True, True, True, False, True]),
        ([4, 2, 1, 1, 2], 1, [True, False, False, False, False]),
    ],
)
def test_basic(candies: list[int], extra: int, expected: list[bool]):
    assert expected == Solution().kidsWithCandies(candies, extra)
