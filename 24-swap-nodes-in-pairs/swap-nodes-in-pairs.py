# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        l = head
        r = head.next

        l.next = self.swapPairs(r.next)
        r.next = l

        return r