# https://leetcode.com/problems/unique-morse-code-words/
import pytest


class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        codes = {
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z": "--..",
        }
        mc_dict = {}
        for word in words:
            mc = ""
            for c in word:
                mc += codes[c]
            if mc in mc_dict:
                pass
            else:
                mc_dict[mc] = 1
        return len(mc_dict)


@pytest.mark.parametrize(("words", "expected"), [(["gin", "zen", "gig", "msg"], 2)])
def test_basic(words: list[str], expected: int):
    assert expected == Solution().uniqueMorseRepresentations(words)
