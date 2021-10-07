# https://leetcode.com/problems/reformat-the-string/
# Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

# You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

# Return the reformatted string or return an empty string if it is impossible to reformat the string.

import pytest


class Solution:
    def reformat(self, s: str) -> str:
        result = ""
        chars = []
        nums = []
        for i in s:
            if i.isalpha():
                chars.append(i)
            else:
                nums.append(i)
        absolute_val = abs(len(chars) - len(nums))
        if absolute_val > 1:
            return ""
        i = 0
        param1 = []
        param2 = []
        param1 = nums
        param2 = chars
        if absolute_val != 0:
            if len(chars) > len(nums):
                param1 = chars
                param2 = nums
            else:
                param1 = nums
                param2 = chars

        while i < len(param1):
            result += param1[i]
            if i < len(param2):
                result += param2[i]
            i += 1
        return result


@pytest.mark.parametrize(
    ("s", "result"),
    [("ab0c12", "0a1b2c"), ("leetcode", ""), ("ab123", "1a2b3"), ("a123", "")],
)
def test_reformat(s: str, result: str) -> None:
    assert result == Solution().reformat(s)
