# https://leetcode.com/problems/1-bit-and-2-bit-characters/
# We have two special characters:
# The first character can be represented by one bit 0.
# The second character can be represented by two bits (10 or 11).
# Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.
import pytest


class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        if i == len(bits) - 1:
            return True
        return False


@pytest.mark.parametrize(
    ("bits", "result"),
    [
        ([1, 0, 0], True),
        ([1, 1, 1, 1, 1, 0], False),
        ([1, 1, 1, 1, 1, 1, 0], True),
        ([1, 1, 0], True),
        ([1, 0], False),
        ([0, 1, 0], False),
    ],
)
def test_basic(bits: list[int], result: bool) -> None:
    assert result == Solution().isOneBitCharacter(bits)
