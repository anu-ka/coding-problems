import re
from tkinter.tix import Tree


class TreeNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        result = []
        if root == None:
            return True
        self.inorder(root, result)
        i = 0
        j = 1
        while j < len(result):
            if result[i] >= result[j]:
                return False
            i += 1
            j = i + 1

        return True

    def inorder(self, root: TreeNode, result: list[int]) -> None:
        if root != None:
            self.inorder(root.left, result)
            result.append(root.val)
            self.inorder(root.right, result)


# five = TreeNode(5)
# one = TreeNode(1)
# four = TreeNode(4)
# three = TreeNode(3)
# six = TreeNode(6)

# five.left = one
# five.right = four
# four.left = three
# four.right = six

# print(isValidBST(five))

# two = TreeNode(2)
# one = TreeNode(1)
# three = TreeNode(3)
# two.left = one
# two.right = three
# print(isValidBST(two))

# [5,4,6,null,null,3,7]
five = TreeNode(5)
four = TreeNode(4)
six = TreeNode(6)
three = TreeNode(3)
seven = TreeNode(7)

five.left = four
five.right = six
six.left = three
six.right = seven
print(Solution().isValidBST(five))
