# https://leetcode.com/problems/build-an-array-with-stack-operations/
# Given an array target and an integer n. In each iteration, you will read a number from  list = {1,2,3..., n}.
# Build the target array using the following operations:
# Push: Read a new element from the beginning list, and push it in the array.
# Pop: delete the last element of the array.
# If the target array is already built, stop reading more elements.
# Return the operations to build the target array. You are guaranteed that the answer is unique.

import pytest


class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        result = []
        push = "Push"
        pop = "Pop"
        i = 1
        counter = 0
        while counter < len(target):
            result.append(push)
            if target[counter] != i:
                result.append(pop)
            else:
                counter += 1
            i += 1
        return result


@pytest.mark.parametrize(
    ("target", "n", "expected"),
    [
        ([1, 3], 3, ["Push", "Push", "Pop", "Push"]),
        ([1, 2, 3], 3, ["Push", "Push", "Push"]),
        ([1, 2], 4, ["Push", "Push"]),
        ([2, 3, 4], 4, ["Push", "Pop", "Push", "Push", "Push"]),
    ],
)
def test_basic(target: list[int], n: int, expected: list[str]):
    assert expected == Solution().buildArray(target, n)
