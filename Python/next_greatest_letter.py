# https://leetcode.com/problems/find-smallest-letter-greater-than-target/
# Given a characters array letters that is sorted in non-decreasing order and a character target,
# return the smallest character in the array that is larger than target.
# Note that the letters wrap around.
# For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.

import pytest


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:

        index = -1
        min = ord("z") + 1
        for i, val in enumerate(letters):
            if ord(val) > ord(target):
                if min > ord(val):
                    min = ord(val)
                    index = i
                    break
        if index == -1:
            return letters[0]

        return letters[index]


@pytest.mark.parametrize(
    ("letters", "target", "expected"),
    [
        (["c", "f", "j"], "a", "c"),
        (["a", "b"], "z", "a"),
        (["a", "b", "i", "k"], "g", "i"),
        (["a", "b", "e", "i"], "g", "i"),
        (["w", "x", "y", "z", "y", "z"], "y", "z"),
    ],
)
def test_basic(letters: list[str], target: str, expected: str) -> None:
    assert expected == Solution().nextGreatestLetter(letters, target)
