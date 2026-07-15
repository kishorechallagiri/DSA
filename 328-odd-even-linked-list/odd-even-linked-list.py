# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        #corner case
        if not head or not head.next:
            return head
        odd=head
        even=head.next
        evenstart=even
        while odd.next and even.next:
            odd.next=odd.next.next
            even.next=even.next.next
            odd=odd.next
            even=even.next
        odd.next=evenstart    
        return head    


        