# https://leetcode.com/problems/design-hashset/

import pytest


class MyHashSet:
    hashset = []

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashset = [-1] * 1_000_001

    def add(self, key: int) -> None:
        self.hashset[key] = key

    def remove(self, key: int) -> None:
        self.hashset[key] = -1

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.hashset[key] == key


def test_hashset() -> None:
    hashset = MyHashSet()
    assert hashset.add(1) == None
    assert hashset.add(2) == None
    assert hashset.contains(1) == True
    assert hashset.contains(3) == False
    assert hashset.add(2) == None
    assert hashset.contains(2) == True
    assert hashset.remove(2) == None
    assert hashset.contains(2) == False
    assert hashset.add(1000000) == None
    assert hashset.remove(1000000) == None
