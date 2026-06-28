# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        if not head:
            return None
        lst=[]
        curr=head
        while curr:
            lst.append(curr.val)
            curr=curr.next
        lst.sort()
        newhead = ListNode(lst[0])
        current = newhead

        for value in lst[1:]:
            current.next = ListNode(value)
            current = current.next

        return newhead    
       