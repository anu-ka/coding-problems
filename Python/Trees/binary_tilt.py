# https://leetcode.com/problems/binary-tree-tilt/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from tkinter.tix import Tree
from turtle import right, tilt
from typing import Optional


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        array_tilts = []
        if root == None:
            return 0
        self.tilt(root, array_tilts)
        return sum(array_tilts)

    def tilt(self, root: Optional[TreeNode], array_tilts: list[int]) -> None:
        if root == None:
            return
        left_sum = self.calculate_sum(root.left)
        right_sum = self.calculate_sum(root.right)
        array_tilts.append(abs(left_sum - right_sum))
        self.tilt(root.left, array_tilts)
        self.tilt(root.right, array_tilts)

    def calculate_sum(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return root.val + self.calculate_sum(root.left) + self.calculate_sum(root.right)


two = TreeNode(2)
four = TreeNode(4)
eight = TreeNode(8)
two.left = four
two.right = eight
one = TreeNode(1)
four.right = one
three = TreeNode(3)
four.left = three
print(Solution().findTilt(two))
