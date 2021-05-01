# A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters,
# return true if sentence is a pangram, or false otherwise.
# https://leetcode.com/problems/check-if-the-sentence-is-pangram/

import pytest


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        items = {}
        for i in sentence:
            items[i] = 1

        return len(items) == 26


@pytest.mark.parametrize(
    ("sentence", "expected"),
    [("thequickbrownfoxjumpsoverthelazydog", True), ("leetcode", False)],
)
def test_basic(sentence: str, expected: bool):
    assert expected == Solution().checkIfPangram(sentence)
