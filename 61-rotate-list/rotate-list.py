# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        length=0
        curr=head
        while curr:
            curr=curr.next
            length+=1
        k=k%length 
        if k==0:
            return head   
        slow=head
        fast=head
        for i in range(k):
            fast=fast.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next
        newHead=slow.next
        fast.next=head
        slow.next=None
        return newHead


        
        


   
      
        