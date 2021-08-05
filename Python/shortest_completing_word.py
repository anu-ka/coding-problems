# https://leetcode.com/problems/shortest-completing-word/
# Given a string licensePlate and an array of strings words, find the shortest completing word in words.
# A completing word is a word that contains all the letters in licensePlate.
# Ignore numbers and spaces in licensePlate, and treat letters as case insensitive.
# If a letter appears more than once in licensePlate,
# then it must appear in the word the same number of times or more.
# For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice.
# Possible completing words are "abccdef", "caaacab", and "cbca".
# Return the shortest completing word in words.
# It is guaranteed an answer exists. If there are multiple shortest completing words,
# return the first one that occurs in words.

import pytest


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        # convert license plate to key-value pairs
        licence_dict = {}
        length = 15
        for i in licensePlate:
            if i.isalpha():
                p = i.lower()
                try:
                    licence_dict[p] += 1
                except KeyError:
                    licence_dict[p] = 1
        index = -1
        i = 0
        for word in words:
            word_dict = {}
            temp_length = 0
            for l in word:
                p = l.lower()
                try:
                    word_dict[p] += 1
                except KeyError:
                    word_dict[p] = 1
                temp_length += 1
            is_present = True
            for l in licence_dict:
                if l in word_dict and word_dict[l] >= licence_dict[l]:
                    continue
                else:
                    is_present = False
                    break
            if is_present and length > temp_length:
                length = temp_length
                index = i

            i += 1

        return words[index]


@pytest.mark.parametrize(
    ("licensePlate", "words", "result"),
    [
        ("1s3 PSt", ["step", "steps", "stripe", "stepple"], "steps"),
        ("1s3 456", ["looks", "pest", "stew", "show"], "pest"),
        (
            "GrC8950",
            [
                "measure",
                "other",
                "every",
                "base",
                "according",
                "level",
                "meeting",
                "none",
                "marriage",
                "rest",
            ],
            "according",
        ),
    ],
)
def test_basic(licensePlate: str, words: list[str], result: str) -> None:
    assert result == Solution().shortestCompletingWord(licensePlate, words)
