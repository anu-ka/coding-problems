# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
# You are given an array of strings words and a string chars.
# A string is good if it can be formed by characters from chars (each character can only be used once).
# Return the sum of lengths of all good strings in words.
import pytest


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        count = 0
        list_words = []
        for word in words:
            dict = {}
            for c in word:
                if c in dict:
                    dict[c] += 1
                else:
                    dict[c] = 1
            list_words.append(dict)
        i = 0
        char_dict = {}
        for c in chars:
            if c in char_dict:
                char_dict[c] += 1
            else:
                char_dict[c] = 1
        for word in list_words:
            canForm = True
            len_word = 0
            for c in word:
                if c not in char_dict or char_dict[c] < word[c]:
                    canForm = False
                    break
                else:
                    len_word += word[c]

            if canForm:
                count += len_word

        return count


@pytest.mark.parametrize(
    ("words", "chars", "expected"),
    [
        (["cat", "bt", "hat", "tree"], "atach", 6),
        (["hello", "world", "leetcode"], "welldonehoneyr", 10),
    ],
)
def test_basic(words: list[str], chars: str, expected: int):
    assert expected == Solution().countCharacters(words, chars)
