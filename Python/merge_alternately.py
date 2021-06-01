# https://leetcode.com/problems/merge-strings-alternately/
# You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.
import pytest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        result = ""
        while i < len(word1) and i < len(word2):
            result += word1[i] + word2[i]
            i += 1
        while i < len(word1):
            result += word1[i]
            i += 1
        while i < len(word2):
            result += word2[i]
            i += 1
        return result


@pytest.mark.parametrize(
    ("word1", "word2", "expected"), [("abc", "pqr", "apbqcr"), ("ab", "pqrs", "apbqrs")]
)
def test_basic(word1: str, word2: str, expected: str) -> None:
    assert expected == Solution().mergeAlternately(word1, word2)
