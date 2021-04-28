# You are given an m x n integer grid accounts where accounts[i][j]
# is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank.
# Return the wealth that the richest customer has.
# A customer's wealth is the amount of money they have in all their bank accounts.
# The richest customer is the customer that has the maximum wealth.
# https://leetcode.com/problems/richest-customer-wealth/
import pytest


class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        wealth = 0
        for bank in accounts:
            temp = 0
            for money in bank:
                temp += money
            if temp > wealth:
                wealth = temp
        return wealth


@pytest.mark.parametrize(
    ("accounts", "expected"),
    [([[2, 8, 7], [7, 1, 3], [1, 9, 5]], 17), ([[1, 5], [7, 3], [3, 5]], 10)],
)
def test_basic(accounts: list[list[int]], expected: int):
    assert expected == Solution().maximumWealth(accounts)
