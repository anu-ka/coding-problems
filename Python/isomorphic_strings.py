# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3811/
# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.

import pytest


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sTot = {}
        tTos = {}
        for i, v in enumerate(s):
            try:
                if sTot[v] != t[i]:
                    return False
            except KeyError:
                sTot[v] = t[i]
            try:
                if tTos[t[i]] != v:
                    return False
            except KeyError:
                tTos[t[i]] = v
        return True


@pytest.mark.parametrize(
    ("s", "t", "isomorphic"),
    [("paper", "title", True), ("abac", "abcd", False), ("foo", "bar", False)],
)
def test_basic(s: str, t: str, isomorphic: bool) -> None:
    assert isomorphic == Solution().isIsomorphic(s, t)
