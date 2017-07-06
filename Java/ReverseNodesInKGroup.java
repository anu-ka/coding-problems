/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        int[] tempArray = new int[k];
        ListNode node = head;
        if (head == null) {
            return null;
        }
        if (k == 0) {
            return head;
        }
        int i = 0;
        ListNode tempNode = head;
        while (node != null && i < k) {
            tempArray[i] = node.val;
            node = node.next;
            ++i;
            if (i == k) {
                i = 0;
                for (int p = k - 1; p >= 0; --p) {
                    tempNode.val = tempArray[p];
                    tempNode = tempNode.next;
                }
            }
        }
        return head;
    }
}