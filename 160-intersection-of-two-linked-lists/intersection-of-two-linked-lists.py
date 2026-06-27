# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        store=set()
        while headB:
            store.add(headB)
            headB=headB.next
        while headA:
            if headA in store:
                return headA
            headA=headA.next
        return None    


        
        