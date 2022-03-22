# https://leetcode.com/problems/binary-tree-right-side-view/
from typing import Optional


class TreeNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        result = []
        if root == None:
            return result
        self.rightorder(root, 1, result)
        return result

    def rightorder(self, root: TreeNode, level: int, result: list[int]) -> None:
        l = level
        if root == None:
            return
        if root != None:
            if len(result) < l:
                result.append(root.val)
            self.rightorder(root.right, l + 1, result)
            self.rightorder(root.left, l + 1, result)


result = []
one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)

# one.left = two
# one.right = three
# three.left = four
# four.left = five

one.left = two
one.right = three
two.right = five
three.right = four
print(Solution().rightSideView(one))
