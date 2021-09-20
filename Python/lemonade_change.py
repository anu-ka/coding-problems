# https://leetcode.com/problems/lemonade-change/
# At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you,
# and order one at a time (in the order specified by bills).
# Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.
# You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

# Note that you don't have any change in hand at first.

# Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with correct change, or false otherwise.

import pytest


class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        fives = 0
        tens = 0
        twentys = 0
        for i in bills:
            if i == 5:
                fives += 1
            elif i == 10:
                tens += 1
                fives -= 1
            else:
                twentys += 1
                if tens == 0:
                    fives -= 3
                else:
                    tens -= 1
                    fives -= 1
            if fives < 0 or tens < 0 or twentys < 0:
                return False

        return True


@pytest.mark.parametrize(
    ("bills", "result"),
    [([5, 5, 5, 10, 20], True), ([5, 5, 10, 10, 20], False), ([5, 5, 10], True)],
)
def test_basic(bills: list[int], result: bool) -> None:
    assert result == Solution().lemonadeChange(bills)
