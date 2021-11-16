# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
import pytest


class Solution:
    def removeDuplicates(self, s: str) -> str:
        i = 0
        j = 1
        while j < len(s):
            if s[i] == s[j]:
                s = s[:i] + s[j + 1 :]
                i -= 1
                if i < 0:
                    i = 0
                j = i + 1
            else:
                i = j
                j = i + 1
        return s


@pytest.mark.parametrize(("s", "result"), [("abbaca", "ca"), ("aa", ""), ("a", "a")])
def test_removeDuplicates(s: str, result: str) -> None:
    assert result == Solution().removeDuplicates(s)
