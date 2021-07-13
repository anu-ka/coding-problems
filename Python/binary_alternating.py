# https://leetcode.com/problems/binary-number-with-alternating-bits/
# Given a positive integer,
# check whether it has alternating bits:
# namely, if two adjacent bits will always have different values.
import pytest


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n == 1:
            return True
        temp = -1
        while n > 0:
            r = n % 2
            n = n // 2
            if temp == r:
                return False
            temp = r

        return True


@pytest.mark.parametrize(
    ("n", "hasAlternatingBits"), [(5, True), (7, False), (11, False)]
)
def test_basic(n: int, hasAlternatingBits: bool) -> None:
    assert hasAlternatingBits == Solution().hasAlternatingBits(n)
