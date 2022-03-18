from turtle import right

import pytest


class solution:
    def isPalindrome(self, vals: str) -> bool:
        left = 0
        right = len(vals) - 1
        while left <= right:
            if not vals[left].isalnum():
                left += 1
                continue
            if not vals[right].isalnum():
                right -= 1
                continue
            if vals[left] != vals[right]:
                return False
            left += 1
            right -= 1
        return True


@pytest.mark.parametrize(
    ("vals", "result"),
    [("ab:cd,dcba", True), ("aba", True), (" ", True), ("abca", False)],
)
def test_isPalindrome(vals: str, result: bool) -> None:
    assert result == solution().isPalindrome(vals)
