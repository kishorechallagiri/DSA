# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        sentinel=ListNode(0)
        sentinel.next=head
        curr=head
        length=0
        while curr:
            length+=1
            curr=curr.next
        prev=sentinel
        for i in range(length-n):
            prev=prev.next
        prev.next=prev.next.next
        return sentinel.next        
        