# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
import pytest


class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        final_price = []
        discount_price = [None] * len(prices)
        i = 0
        while i < len(prices):
            discount = 0
            j = i + 1
            while j < len(prices):
                if prices[j] <= prices[i]:
                    discount = prices[j]
                    break
                j += 1
            discount_price[i] = discount
            i += 1

        k = 0
        while k < len(prices):
            final_price.append(prices[k] - discount_price[k])
            k += 1
        return final_price


@pytest.mark.parametrize(
    ("prices", "expected"),
    [([8, 4, 6, 2, 3], [4, 2, 4, 2, 3]), ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])],
)
def test_basic(prices: list[int], expected: list[int]):
    assert expected == Solution().finalPrices(prices)
