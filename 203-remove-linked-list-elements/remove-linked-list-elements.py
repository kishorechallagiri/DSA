# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        sentinel=ListNode(0)
        sentinel.next=head
        curr=sentinel
        while curr and curr.next:
            if curr.next.val==val:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return sentinel.next            

        