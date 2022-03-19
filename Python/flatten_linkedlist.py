from typing import Optional


class doublyLinkedList:
    def __init__(self, val: int) -> None:
        self.val = val
        self.prev = None
        self.next = None
        self.child = None


class Solution:
    def flatten_list(self, root: Optional[doublyLinkedList]) -> doublyLinkedList:
        if root == None:
            return
        result = doublyLinkedList(root.val)
        curr = result
        temp_stack = []
        while root != None or len(temp_stack) > 0:
            if root != None:
                if root.child != None:
                    if root.next != None:
                        temp_stack.append(root.next)
                    curr.next = doublyLinkedList(root.child.val)
                    curr.next.prev = curr
                    curr = curr.next

                    root = root.child

                    continue
                if root.next != None:
                    curr.next = doublyLinkedList(root.next.val)
                    curr.next.prev = curr
                    curr = curr.next
                root = root.next
            elif len(temp_stack) > 0:
                temp = temp_stack.pop()
                curr.next = doublyLinkedList(temp.val)
                curr.next.prev = curr
                curr = curr.next
                root = temp
        return result


one = doublyLinkedList(1)
two = doublyLinkedList(2)
three = doublyLinkedList(3)
four = doublyLinkedList(4)
five = doublyLinkedList(5)
six = doublyLinkedList(6)
seven = doublyLinkedList(7)
eight = doublyLinkedList(8)
nine = doublyLinkedList(9)
ten = doublyLinkedList(10)
eleven = doublyLinkedList(11)

one.next = two
two.prev = one
two.next = three
three.prev = two
three.next = four
four.prev = three
four.next = five
five.prev = four
five.next = six
six.prev = five

seven.next = eight
eight.prev = seven
eight.next = nine
nine.prev = eight

ten.next = eleven
eleven.prev = ten

two.child = seven
eight.child = ten
nodes = Solution().flatten_list(one)
while nodes != None:
    print(nodes.val)
    nodes = nodes.next
