# https://leetcode.com/problems/minimum-index-sum-of-two-lists/
# Suppose Andy and Doris want to choose a restaurant for dinner,
# and they both have a list of favorite restaurants represented by strings.
# You need to help them find out their common interest with the least list index sum.
# If there is a choice tie between answers, output all of them with no order requirement.
# You could assume there always exists an answer.

import pytest


class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        result = {}
        dict_vals = {}
        for i, val in enumerate(list1):
            dict_vals[val] = i

        for i, val in enumerate(list2):
            if val in dict_vals:
                result[val] = i + dict_vals[val]

        final = []
        min = list(result.values())[0]
        for i in result:
            if result[i] < min:
                min = result[i]
        for i in result:
            if min == result[i]:
                final.append(i)
        return final


@pytest.mark.parametrize(
    ("list1", "list2", "expected"),
    [
        (
            ["Shogun", "Tapioca Express", "Burger King", "KFC"],
            [
                "Piatti",
                "The Grill at Torrey Pines",
                "Hungry Hunter Steakhouse",
                "Shogun",
            ],
            ["Shogun"],
        ),
        (
            ["Shogun", "Tapioca Express", "Burger King", "KFC"],
            ["KFC", "Shogun", "Burger King"],
            ["Shogun"],
        ),
        (
            ["Shogun", "Tapioca Express", "Burger King", "KFC"],
            ["KFC", "Burger King", "Tapioca Express", "Shogun"],
            ["KFC", "Burger King", "Tapioca Express", "Shogun"],
        ),
        (["KFC"], ["KFC"], ["KFC"]),
    ],
)
def test_basic(list1: list[str], list2: list[str], expected: list[str]) -> None:
    assert expected == Solution().findRestaurant(list1, list2)


# list1 =
# list2 =
list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Shogun", "Burger King"]
