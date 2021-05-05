# Given two string arrays word1 and word2,
# return true if the two arrays represent the same string, and false otherwise.
# A string is represented by an array if the array elements concatenated in order forms the string.
# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

import pytest


class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        list1 = []
        list2 = []
        for w in word1:
            for l in w:
                list1.append(l)

        for w in word2:
            for l in w:
                list2.append(l)

        return list1 == list2


@pytest.mark.parametrize(
    ("word1", "word2", "expected"),
    [(["ab", "c"], ["a", "bc"], True), (["a", "cb"], ["ab", "c"], False)],
)
def test_basic(word1: list[str], word2: list[str], expected: bool):
    assert expected == Solution().arrayStringsAreEqual(word1, word2)


a = ["ab", "c"]
b = ["a", "bc"]
print(Solution().arrayStringsAreEqual(a, b))
