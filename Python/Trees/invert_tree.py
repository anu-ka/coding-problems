from operator import invert
from tkinter.tix import Tree
from typing import Optional


class TreeNode:
    def __init__(self, val: int, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        head = root
        self.invertnow(root, root.left, root.right)
        return head

    def invertnow(self, parent: TreeNode, left: TreeNode, right: TreeNode):
        if left == None and right == None:
            return
        temp = left
        parent.left = right
        parent.right = temp
        if left != None:
            self.invertnow(left, left.left, left.right)
        if right != None:
            self.invertnow(right, right.left, right.right)


one = TreeNode(1)
two = TreeNode(2)
# three = TreeNode(3)
# four = TreeNode(4)
# five = TreeNode(5)
# six = TreeNode(6)
# seven = TreeNode(7)
one.left = two
# two.left = four
# two.right = five
# one.right = three
# three.left = six
# three.right = seven


def printHead(head: TreeNode):
    if head == None:
        return
    print(head.val)
    print(f"Going left")
    printHead(head.left)
    print("Going right")
    printHead(head.right)


head = Solution().invertTree(one)
printHead(head)
