# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
# Given a sentence that consists of some words separated by a single space, and a searchWord,
# check if searchWord is a prefix of any word in sentence.
# Return the index of the word in sentence (1-indexed) where searchWord is a prefix of this word.
# If searchWord is a prefix of more than one word,
# return the index of the first word (minimum index). If there is no such word return -1.
# A prefix of a string s is any leading contiguous substring of s.

import pytest


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(" ")
        for i, word in enumerate(words):
            if word.startswith(searchWord):
                return i + 1
        return -1


@pytest.mark.parametrize(
    ("sentence", "searchWord", "result"),
    [("i love eating burger", "burg", 4), ("i am tired", "you", -1)],
)
def test_basic(sentence: str, searchWord: str, result: int) -> None:
    assert result == Solution().isPrefixOfWord(sentence, searchWord)
