# https://leetcode.com/problems/decode-xored-array/
# There is a hidden integer array arr that consists of n non-negative integers.
# It was encoded into another integer array encoded of length n - 1, such that encoded[i] = arr[i] XOR arr[i + 1]. For example, if arr = [1,0,2,1], then encoded = [1,2,3].
# You are given the encoded array. You are also given an integer first, that is the first element of arr, i.e. arr[0].
# Return the original array arr. It can be proved that the answer exists and is unique.

import pytest


class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        i = 0
        result = [first]
        while i < len(encoded):
            val = first ^ encoded[i]
            result.append(val)
            first = val
            i += 1
        return result


@pytest.mark.parametrize(
    ("encoded", "first", "expected"), [([1, 2, 3], 1, [1, 0, 2, 1])]
)
def test_basic(encoded: list[int], first: int, expected: list[int]):
    assert expected == Solution().decode(encoded, first)
