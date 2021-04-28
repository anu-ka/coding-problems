# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
# https://leetcode.com/problems/reverse-integer/

import pytest


class Solution:
    def reverse(self, x: int) -> int:
        isnegative = x < 0
        x = -x if isnegative else x

        if x < 10:
            return -x if isnegative else x
        lower = -2147483648
        upper = 2147483647
        num = x
        r = 0
        while num > 0:
            r = r * 10
            r += num % 10
            num = num // 10
            if r <= lower or r >= upper:
                return 0
        if isnegative:
            r = r * -1
        return r


@pytest.mark.parametrize(
    ("num", "expected"),
    [(7463847412, 0), (-2147483648, 0), (123, 321), (120, 21), (-15, -51)],
)
def test_basic(num: int, expected: int):
    Solution().reverse(num)
