/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        if(l1==null && l2==null) {
            return null;
        }
        if(l1==null && l2!=null) {
            return l2;
        }
        if (l2 == null && l1 != null) {
            return l1;
        }
        ListNode resultNode=null;
        ListNode node = null;
        int carryOver = 0;
        int prevcarryOver = 0;
        int result = 0;
        while(l1!=null && l2!=null) {
            int s = l1.val + l2.val + prevcarryOver;
            carryOver = s / 10;
            result = s % 10;
            if(node==null) {
                node = new ListNode(result);
                resultNode = node;
            }
            else {
                node.next = new ListNode(result);
                node = node.next;
            }
            prevcarryOver = carryOver;
            l1 = l1.next;
            l2 = l2.next;
        }
        if(l1==null && l2==null) {
            if(prevcarryOver>0)
            node.next = new ListNode(prevcarryOver);
            return resultNode;
        }
        if(l1==null) {
            AddNumbers(prevcarryOver, node, l2);
        }
        else if(l2==null) {
            AddNumbers(prevcarryOver, node, l1);
        }
        return resultNode;
    }
    
    private static void AddNumbers(int prevcarryOver, ListNode node, ListNode l2) {
        int result = 0;
        int carryOver = 0;
        while(l2!=null) {
            int s = l2.val + prevcarryOver;
            carryOver = s / 10;
            result = s % 10;
            node.next = new ListNode(result);
            node = node.next;
            l2 = l2.next;
            prevcarryOver = carryOver;
        }
        if(prevcarryOver>0) {
            node.next = new ListNode(prevcarryOver);
        }
    }

}