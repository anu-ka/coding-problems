# https://leetcode.com/problems/split-a-string-in-balanced-strings/
# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
# Given a balanced string s, split it in the maximum amount of balanced strings.
# Return the maximum amount of split balanced strings.

import pytest


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = []
        temp = ""
        count = 0
        for i in s:
            if len(stack) == 0 or stack[0] == i:
                stack.append(i)
                temp = i
            else:
                stack.remove(temp)
                if len(stack) == 0:
                    count += 1
        return count


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("LR", 1),
        ("RRLLLLRR", 2),
        ("RLRRLLRLRL", 4),
        ("LLRRLLRRLLLRRRRL", 4),
        ("RLLLLRRRLR", 3),
        ("LLLLRRRR", 1),
    ],
)
def test_basic(s: str, expected: int) -> None:
    assert expected == Solution().balancedStringSplit(s)
