# https://leetcode.com/problems/delete-columns-to-make-sorted/
# You are given an array of n strings strs, all of the same length.
# The strings can be arranged such that there is one on each line, making a grid.
# For example, strs = ["abc", "bce", "cae"] can be arranged as:
# abc
# bce
# cae
# You want to delete the columns that are not sorted lexicographically.
# In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted
# while column 1 ('b', 'c', 'a') is not, so you would delete column 1.
# Return the number of columns that you will delete.
import pytest


class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        count = 0
        i = 0
        j = 0
        length = len(strs[0])
        while i < length:
            j = 1
            prev = strs[0][i]
            while j < len(strs):
                if strs[j][i] < prev:
                    count += 1
                    break
                prev = strs[j][i]
                j += 1
            i += 1

        return count


@pytest.mark.parametrize(
    ("strs", "expected"),
    [
        (["aee", "baf", "cdf"], 1),
        (["cba", "daf", "ghi"], 1),
        (["a", "b"], 0),
        (["zyx", "wvu", "tsr"], 3),
        (["rrjk", "furt", "guzm"], 2),
    ],
)
def test_basic(strs: list[str], expected: int) -> None:
    assert expected == Solution().minDeletionSize(strs)
