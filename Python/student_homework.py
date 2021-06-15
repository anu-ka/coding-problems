# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/
# Given two integer arrays startTime and endTime and given an integer queryTime.
# The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].
# Return the number of students doing their homework at time queryTime.
# More formally, return the number of students where queryTime lays in the interval [startTime[i],
# endTime[i]] inclusive.

import pytest


class Solution:
    def busyStudent(
        self, startTime: list[int], endTime: list[int], queryTime: int
    ) -> int:
        count = 0
        for i, _ in enumerate(startTime):
            if startTime[i] <= queryTime and queryTime <= endTime[i]:
                count += 1
        return count


@pytest.mark.parametrize(
    ("startTime", "endTime", "queryTime", "expected"),
    [
        ([1, 2, 3], [3, 2, 7], 4, 1),
        ([4], [4], 4, 1),
        ([1, 1, 1, 1], [1, 3, 2, 4], 7, 0),
        ([9, 8, 7, 6, 5, 4, 3, 2, 1], [10, 10, 10, 10, 10, 10, 10, 10, 10], 5, 5),
    ],
)
def test_basic(
    startTime: list[int], endTime: list[int], queryTime: int, expected: int
) -> None:
    assert expected == Solution().busyStudent(startTime, endTime, queryTime)
