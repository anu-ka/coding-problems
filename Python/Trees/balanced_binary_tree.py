# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        if (
            abs(
                self.height_binary_tree(root.left) - self.height_binary_tree(root.right)
            )
            > 1
        ):
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height_binary_tree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return 1 + max(
            self.height_binary_tree(root.left), self.height_binary_tree(root.right)
        )


root1 = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
root1.left = two
root1.right = three
four = TreeNode(4)
two.left = four
print(Solution().isBalanced(root1))
