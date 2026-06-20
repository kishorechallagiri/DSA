# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        dummy=ListNode()
        dummy.next=head
        p=dummy
        c=head
        n=head.next
        while c and n:
            p.next=n
            c.next=n.next
            n.next=c
            p=c
            c=p.next
            n=c.next if c else None
        return dummy.next    
       