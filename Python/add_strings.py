# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/614/week-2-august-8th-august-14th/3875/
# Given two non-negative integers, num1 and num2 represented as string,
# return the sum of num1 and num2 as a string.
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
# You must also not convert the inputs to integers directly.

import pytest


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        if not num1:
            return num2
        if not num2:
            return num1
        result = ""
        dict_nums = {}
        for i in range(0, 10):
            dict_nums[str(i)] = i
        i = len(num1) - 1
        j = len(num2) - 1
        rem = 0
        while i >= 0 or j >= 0 or rem > 0:
            n1 = "0"
            n2 = "0"
            if i >= 0:
                n1 = num1[i]
            if j >= 0:
                n2 = num2[j]
            sum = dict_nums[n1] + dict_nums[n2] + rem
            rem = sum // 10
            sum = sum % 10
            result = str(sum) + result
            i -= 1
            j -= 1

        return result


@pytest.mark.parametrize(
    ("num1", "num2", "result"),
    [("0", "0", "0"), ("11", "123", "134"), ("456", "77", "533")],
)
def test_basic(num1: str, num2: str, result: str) -> None:
    assert result == Solution().addStrings(num1, num2)
