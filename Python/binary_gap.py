# https://leetcode.com/problems/binary-gap/
# Given a positive integer n,
# find and return the longest distance between any two adjacent 1's in the binary representation of n.
# If there are no two adjacent 1's, return 0.
# Two 1's are adjacent if there are only 0's separating them (possibly no 0's).
# The distance between two 1's is the absolute difference between their bit positions.
# For example, the two 1's in "1001" have a distance of 3.
import pytest


class Solution:
    def binaryGap(self, n: int) -> int:
        # convert the number to binary
        index = 0
        temp_arr = []
        while n > 0:
            r = n % 2
            n = n // 2
            if r == 1:
                temp_arr.append(index)
            index += 1

        count = 0
        i = 0
        while i + 1 < len(temp_arr):
            if temp_arr[i + 1] - temp_arr[i] > count:
                count = temp_arr[i + 1] - temp_arr[i]
            i += 1

        return count


@pytest.mark.parametrize(
    ("n", "count"), [(22, 2), (5, 2), (6, 1), (8, 0), (1, 0), (1000000000, 3)]
)
def test_basic(n: int, count: int) -> None:
    assert count == Solution().binaryGap(n)
