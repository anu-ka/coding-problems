# https://leetcode.com/problems/maximum-number-of-balloons/
# Given a string text, you want to use the characters of text to form as many instances of the word
# "balloon" as possible.You can use each character in text at most once.
# Return the maximum number of instances that can be formed.
import pytest


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dict_balloon = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
        for i in text:
            if i in dict_balloon:
                dict_balloon[i] += 1
        l = dict_balloon["l"] // 2
        dict_balloon["l"] = l
        o = dict_balloon["o"] // 2
        dict_balloon["o"] = o

        count = 10000
        for i in dict_balloon:
            if dict_balloon[i] < count:
                count = dict_balloon[i]
        return count


@pytest.mark.parametrize(
    ("text", "result"), [("loonbalxballpoon", 2), ("leetcode", 0), ("nlaebolko", 1)]
)
def test_basic(text: str, result: int) -> None:
    assert result == Solution().maxNumberOfBalloons(text)
