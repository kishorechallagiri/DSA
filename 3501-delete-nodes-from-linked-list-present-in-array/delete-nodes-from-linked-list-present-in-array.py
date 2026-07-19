# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        dummy=ListNode()
        dummyHead=dummy
        hash=set()
        for num in nums:
            hash.add(num)
        curr=head
        while curr :
            if curr.val not in hash:
                dummy.next=curr
                dummy=dummy.next
            curr=curr.next
        dummy.next=None    
        return dummyHead.next    


