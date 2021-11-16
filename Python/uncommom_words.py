# https://leetcode.com/problems/uncommon-words-from-two-sentences/
import pytest


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        result = []
        dict_values = {}
        self.fillDictionary(s1, dict_values)
        self.fillDictionary(s2, dict_values)

        for i in dict_values:
            if dict_values[i] == 1:
                result.append(i)
        return result

    def fillDictionary(self, s: str, dict_values: dict) -> None:
        vals = s.split(" ")
        for i in vals:
            try:
                dict_values[i] += 1
            except KeyError:
                dict_values[i] = 1


@pytest.mark.parametrize(
    ("s1", "s2", "result"),
    [
        ("this apple is sweet", "this apple is sour", ["sweet", "sour"]),
        ("banana banana", "apple", ["apple"]),
    ],
)
def test_uncommonFromSentences(s1: str, s2: str, result: list[str]) -> None:
    assert result == Solution().uncommonFromSentences(s1, s2)
