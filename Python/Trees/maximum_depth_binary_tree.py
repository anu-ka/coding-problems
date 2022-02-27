# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        if root.left == None and root.right != None:
            return 1 + self.minDepth(root.right)
        if root.left != None and root.right == None:
            return 1 + self.minDepth(root.left)
        if root.left != None and root.right != None:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
one.left = two
one.right = three
four = TreeNode(4)
two.left = four
# print(Solution().minDepth(one))
print(Solution().minDepth(one))
