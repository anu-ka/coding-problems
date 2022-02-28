# https://leetcode.com/problems/minimum-distance-between-bst-nodes/
# Definition for a binary tree node.
from pickletools import optimize
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        list_vals = []
        self._in_traversal(root, list_vals)
        min = list_vals[len(list_vals) - 1]

        i = 0
        while i < len(list_vals) - 1:
            if list_vals[i + 1] - list_vals[i] < min:
                min = list_vals[i + 1] - list_vals[i]
            i += 1
        return min

    def _in_traversal(self, root: Optional[TreeNode], list_vals: list[int]) -> None:

        if root != None:
            self._in_traversal(root.left, list_vals)
            list_vals.append(root.val)
            self._in_traversal(root.right, list_vals)


two = TreeNode(2)
one = TreeNode(1)
four = TreeNode(4)
two.left = one
two.right = four
print(Solution().minDiffInBST(two))
