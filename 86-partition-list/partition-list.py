# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        small=ListNode()
        smallHead=small
        big=ListNode() 
        bigHead=big
        curr=head
        while curr:
            if curr.val<x:
                small.next=curr
                small=small.next
            else:
                big.next=curr
                big=big.next
            curr=curr.next
        big.next=None
        small.next=bigHead.next
        return smallHead.next




         