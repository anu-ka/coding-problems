# https://leetcode.com/problems/find-common-characters/
# Given a string array words, return an array of all characters that show up in
# all strings within the words (including duplicates). You may return the answer in any order.

import pytest


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        result = []
        list_words = []
        for word in words:
            dict_temp = {}
            for c in word:
                try:
                    dict_temp[c] += 1
                except KeyError:
                    dict_temp[c] = 1
            list_words.append(dict_temp)
        i = 0
        j = 1
        while j < len(list_words):
            dict_temp = {}
            for c in list_words[i]:
                if c in list_words[j]:
                    dict_temp[c] = min(list_words[i][c], list_words[j][c])
            list_words[j] = dict_temp
            i += 1
            j += 1
        res = list_words[j - 1]
        for c in res:
            i = res[c]
            while i > 0:
                result.append(c)
                i -= 1

        return result


@pytest.mark.parametrize(
    ("words", "result"),
    [
        (["bella", "label", "roller"], ["e", "l", "l"]),
        (["cool", "lock", "cook"], ["c", "o"]),
    ],
)
def test_commonChars(words: list[str], result: list[str]) -> None:
    assert result == Solution().commonChars(words)
