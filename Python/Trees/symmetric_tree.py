# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from tkinter.messagebox import NO
from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.areSame(root.left, root.right)

    def areSame(self, left: TreeNode, right: TreeNode) -> bool:
        if (left == None and right != None) or (left != None and right == None):
            return False
        if left == None and right == None:
            return True
        if left.val != right.val:
            return False
        return self.areSame(left.left, right.right) and self.areSame(
            left.right, right.left
        )


root = TreeNode(1)
two_left = root.left = TreeNode(2)
two_right = root.right = TreeNode(2)
three_left = two_left.left = TreeNode(3)
three_right = two_right.right = TreeNode(3)

print(Solution().isSymmetric(root))
