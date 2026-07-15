# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        sentinel=ListNode(0)
        sentinel.next=head
        first=sentinel
        for i in range(n):
            first=first.next
        second=sentinel
        while first.next:
            second=second.next
            first=first.next
        second.next=second.next.next
        return sentinel.next        
        