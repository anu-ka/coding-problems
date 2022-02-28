# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        l_h = self._height_binaryTree(root.left)
        r_h = self._height_binaryTree(root.right)

        if l_h + r_h > self.diameter:
            self.diameter = l_h + r_h
        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)
        return self.diameter

    def _height_binaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if root != None:
            return 1 + max(
                self._height_binaryTree(root.left),
                (self._height_binaryTree(root.right)),
            )


one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
one.left = two
two.left = three
one.right = four
print(Solution().diameterOfBinaryTree(one))
