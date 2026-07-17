# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        hash={}
        dummy=ListNode()
        dummyHead=dummy
        curr=head
        while curr:
            if curr.val not in hash:
                hash[curr.val]=1
                curr=curr.next
            else:
                hash[curr.val]+=1
                curr=curr.next
        curr=head
        while curr:
            if hash[curr.val]==1:
                dummy.next=curr
                dummy=dummy.next
            curr=curr.next
        dummy.next=None
        return dummyHead.next                    
        