# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        if not head or not head.next:
            return head
        dummy=ListNode()
        dummy.next=head
        prev=dummy
        for i in range(left-1):
            prev=prev.next
        curr=prev.next
        for i in range(right-left):
            nxt=curr.next
            curr.next=nxt.next
            nxt.next=prev.next
            prev.next=nxt
        return dummy.next        

        