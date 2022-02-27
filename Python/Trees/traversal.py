# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from tkinter.tix import Tree
from typing import Optional


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        # left->root->right
        result = []
        self.inorder(root, result)
        return result

    def inorder(self, root: Optional[TreeNode], result: list[int]) -> None:
        if root != None:
            self.inorder(root.left, result)
            result.append(root.val)
            self.inorder(root.right, result)

    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        result = []
        self.preorder(root, result)
        return result

    def preorder(self, root: Optional[TreeNode], result: list[int]) -> None:
        if root != None:
            result.append(root.val)
            self.preorder(root.left, result)
            self.preorder(root.right, result)

    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        result = []
        self.postorder(root, result)
        return result

    def postorder(self, root: Optional[TreeNode], result: list[int]) -> None:
        if root != None:
            self.postorder(root.left, result)
            self.postorder(root.right, result)
            result.append(root.val)


one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
one.left = two
one.right = three
four = TreeNode(4)
two.left = four
print(Solution().inorderTraversal(one))
print(Solution().preorderTraversal(one))
