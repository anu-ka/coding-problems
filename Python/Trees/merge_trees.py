# Definition for a binary tree node.
# https://leetcode.com/problems/merge-two-binary-trees/
# You are given two binary trees root1 and root2.
# Imagine that when you put one of them to cover the other,
# some nodes of the two trees are overlapped while the others are not.
# You need to merge the two trees into a new binary tree.
# The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node.
# Otherwise, the NOT null node will be used as the node of the new tree.
# Return the merged tree.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from tkinter.messagebox import NO
from typing import Optional


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        result = TreeNode()
        if root1 == None and root2 == None:
            return None

        elif root1 != None and root2 != None:
            result.val = root1.val + root2.val
            result.left = self.mergeTrees(root1.left, root2.left)
            result.right = self.mergeTrees(root1.right, root2.right)
        elif root1 != None and root2 == None:
            result.val = root1.val
            result.left = self.mergeTrees(root1.left, None)
            result.right = self.mergeTrees(root1.right, None)
        elif root1 == None and root2 != None:
            result.val = root2.val
            result.left = self.mergeTrees(None, root2.left)
            result.right = self.mergeTrees(None, root2.right)
        return result


root1 = TreeNode(1)
two = TreeNode(2)
# three = TreeNode(3)
root1.left = two
# root1.right = three

root2 = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)
root2.left = four
root2.right = five

head = Solution().mergeTrees(root1, root2)
print(head.val)
