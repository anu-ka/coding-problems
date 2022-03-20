# https://leetcode.com/problems/linked-list-cycle-ii/
from typing import Optional


class LinkedList:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class solution:
    def detectCycle(self, root: Optional[LinkedList]) -> LinkedList:
        if root != None and root.next != None:
            if root == root.next.next:
                return root

        temp_dict = {}
        while root != None and root.next != None:
            next = root.next
            try:
                temp_dict[next].append(root)
                return next
            except KeyError:
                temp_dict[next] = [root]
            root = root.next

        return None


one = LinkedList(1)
two = LinkedList(2)
# three = LinkedList(3)

one.next = two
two.next = one
# three.next = one

three = LinkedList(3)
two = LinkedList(2)
zero = LinkedList(0)
minusfour = LinkedList(-4)

three.next = two
two.next = zero
zero.next = minusfour
minusfour.next = two

# nodes = solution().detectCycle(three)
nodes = solution().detectCycle(one)

while nodes != None:
    print(nodes.val)
    nodes = nodes.next
