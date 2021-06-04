# https://leetcode.com/problems/fibonacci-number/
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

import pytest


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        dict_fib = {}
        dict_fib[0] = 0
        dict_fib[1] = 1
        return self.calculateFib(n, dict_fib)

    def calculateFib(self, n: int, dict_fib: dict) -> int:
        try:
            return dict_fib[n]
        except:
            t = self.calculateFib(n - 2, dict_fib) + self.calculateFib(n - 1, dict_fib)
            dict_fib[n] = t

        return dict_fib[n]


@pytest.mark.parametrize(("n", "expected"), [(0, 0), (1, 1), (2, 1), (3, 2)])
def test_basic(n: int, expected: int) -> None:
    assert expected == Solution().fib(n)


print(Solution().fib(3))
