# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        i = headA
        j = headB
        while i!=j:
            i = i.next if i else headB
            j = j.next if j else headA
        return i    


            


        