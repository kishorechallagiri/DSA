# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        curr=slow
        prev=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        firstlist=head
        secondlist=prev   
        while secondlist:
            if firstlist.val!=secondlist.val:
                return False
            firstlist=firstlist.next
            secondlist=secondlist.next
        return True            
        