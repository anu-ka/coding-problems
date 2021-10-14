# https://leetcode.com/problems/valid-mountain-array/
import pytest


class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        if len(arr) < 3:
            return False
        i = 0
        j = 1
        isIncreasing = False
        while j < len(arr):
            if arr[i] < arr[j]:
                isIncreasing = True
            else:
                break

            i += 1
            j += 1
        if j == len(arr) or arr[i] == arr[j]:
            return False

        while j < len(arr):
            if arr[j] > arr[i] or arr[i] == arr[j]:
                return False
            i += 1
            j += 1
        return isIncreasing


@pytest.mark.parametrize(
    ("arr", "result"),
    [
        ([0, 3, 2, 1], True),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], False),
        ([9, 8, 7, 6, 5, 4], False),
        ([0, 3, 2, 1], True),
        (
            [
                14,
                82,
                89,
                84,
                79,
                70,
                70,
                68,
                67,
                66,
                63,
                60,
                58,
                54,
                44,
                43,
                32,
                28,
                26,
                25,
                22,
                15,
                13,
                12,
                10,
                8,
                7,
                5,
                4,
                3,
            ],
            False,
        ),
    ],
)
def test_validMountainArray(arr: list[int], result: bool) -> None:
    assert result == Solution().validMountainArray(arr)
