# https://leetcode.com/problems/middle-of-the-linked-list/submissions/
# Given a non-empty, singly linked list with head node head, return a middle node of linked list.
# If there are two middle nodes, return the second middle node.

import pytest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        result_node = None
        temp_nodes = {}
        temp = head
        i = 0
        while temp != None:
            temp_nodes[i] = temp
            temp = temp.next
            i += 1
        mid = len(temp_nodes) // 2
        head = temp_nodes[mid]
        return head


listnode1 = ListNode(1)
listnode2 = ListNode(2)
listnode3 = ListNode(3)
listnode1.next = listnode2
listnode2.next = listnode3

expected = listnode2


@pytest.mark.parametrize(("head", "expected"), [(listnode1, expected)])
def test_basic(head: ListNode, expected: ListNode):
    assert expected == Solution().middleNode(head)
