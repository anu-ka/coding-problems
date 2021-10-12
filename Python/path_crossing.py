# https://leetcode.com/problems/path-crossing/
import pytest


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = (0, 0)
        dirs = {}
        dirs[(0, 0)] = 1

        for direction in path:
            if direction == "N":
                y += 1
            elif direction == "E":
                x += 1
            elif direction == "W":
                x -= 1
            elif direction == "S":
                y -= 1
            if (x, y) in dirs:
                return True
            dirs[(x, y)] = 1

        return False


@pytest.mark.parametrize(("path", "result"), [("NES", False), ("NESWW", True)])
def test_isPathCrossing(path: str, result: bool) -> None:
    assert result == Solution().isPathCrossing(path)
