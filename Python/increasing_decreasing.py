# https://leetcode.com/problems/increasing-decreasing-string/
# Given a string s. You should re-order the string using the following algorithm:
# Pick the smallest character from s and append it to the result.
# Pick the smallest character from s which is greater than the last appended character to the result and append it.
# Repeat step 2 until you cannot pick more characters.
# Pick the largest character from s and append it to the result.
# Pick the largest character from s which is smaller than the last appended character to the result and append it.
# Repeat step 5 until you cannot pick more characters.
# Repeat the steps from 1 to 6 until you pick all characters from s.
# In each step,
# If the smallest or the largest character appears more than once you can choose any occurrence and
# append it to the result.
# Return the result string after sorting s with this algorithm.

import pytest


class Solution:
    def sortString(self, s: str) -> str:
        result = ""
        temp = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,
            "h": 0,
            "i": 0,
            "j": 0,
            "k": 0,
            "l": 0,
            "m": 0,
            "n": 0,
            "o": 0,
            "p": 0,
            "q": 0,
            "r": 0,
            "s": 0,
            "t": 0,
            "u": 0,
            "v": 0,
            "w": 0,
            "x": 0,
            "y": 0,
            "z": 0,
        }
        for char in s:
            temp[char] += 1
        stringFreq = {}
        for item in temp:
            if temp[item] > 0:
                stringFreq[item] = temp[item]
        topdown = True
        while len(stringFreq) > 0:
            tempStr = ""
            for item in stringFreq:
                if stringFreq[item] > 0:
                    tempStr += item
                    stringFreq[item] -= 1
            if topdown:
                result += tempStr
                topdown = False
            else:
                result += tempStr[::-1]
                topdown = True
            newDict = {}
            for item in stringFreq:
                if stringFreq[item] > 0:
                    newDict[item] = stringFreq[item]

            stringFreq = newDict
        return result


@pytest.mark.parametrize(
    ("inputString", "expected"),
    [("aaaabbbbcccc", "abccbaabccba"), ("leetcode", "cdelotee")],
)
def test_basic(inputString: str, expected: str):
    assert expected == Solution().sortString(inputString)
