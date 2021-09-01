# https://leetcode.com/problems/reverse-only-letters/
# Given a string s, reverse the string according to the following rules:
# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.

import pytest


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        result = ""
        temp = ""
        i = len(s) - 1
        while i >= 0:
            if s[i].isalpha():
                temp += s[i]
            i -= 1
        k = 0
        p = 0
        while k < len(s):
            if not s[k].isalpha():
                result += s[k]
            else:
                result += temp[p]
                p += 1
            k += 1

        return result


@pytest.mark.parametrize(
    ("input", "result"),
    [
        ("ab-cd", "dc-ba"),
        ("a-bC-dEf-ghIj", "j-Ih-gfE-dCba"),
        ("Test1ng-Leet=code-Q!", "Qedo1ct-eeLg=ntse-T!"),
    ],
)
def test_basic(input: str, result: str) -> None:
    assert result == Solution().reverseOnlyLetters(input)
