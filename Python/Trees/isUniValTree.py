# Definition for a binary tree node.
from tkinter.messagebox import NO
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        return self.checkUniVal(root, root.val)

    def checkUniVal(self, root: Optional[TreeNode], rootval: int) -> bool:
        if root == None:
            return True
        if root.val != rootval:
            return False
        if root.left == None and root.right == None:
            return True
        return self.checkUniVal(root.left, rootval) and self.checkUniVal(
            root.right, root.val
        )
