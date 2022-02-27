from tkinter.tix import Tree
from typing import Optional


class TreeNode:
    def __init__(self, val: int, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        if root == None:
            return []
        result = []
        self.check_path(root, result, "")
        return result

    def check_path(self, root: Optional[TreeNode], result: list[str], res: str) -> None:
        if root == None:
            return
        res += str(root.val)
        res += "->"
        if root.left == None and root.right == None:
            p = res[0 : len(res) - 2]
            result.append(p)
            return
        self.check_path(root.left, result, res)
        self.check_path(root.right, result, res)


one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
one.left = two
one.right = three
four = TreeNode(4)
two.left = four
print(Solution().binaryTreePaths(one))


# 2             3
# 1->2, 1->3
