# https://leetcode.com/problems/robot-return-to-origin/
# There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves,
# judge if this robot ends up at (0, 0) after it completes its moves.
# The move sequence is represented by a string, and the character moves[i] represents its ith move.
# Valid moves are R (right), L (left), U (up), and D (down).
# If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.

import pytest


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = (0, 0)

        for m in moves:
            if m == "U":
                x += 1
            elif m == "D":
                x -= 1
            else:
                if m == "L":
                    y -= 1
                elif m == "R":
                    y += 1
        if x == 0 and y == 0:
            return True
        return False


@pytest.mark.parametrize(
    ("moves", "expected"), [("UD", True), ("LL", False), ("RRDD", False)]
)
def test_basic(moves: str, expected: bool):
    assert expected == Solution().judgeCircle(moves)
