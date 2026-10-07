# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        n = 0
        p = headA

        while p:
            n += 1
            p = p.next

        m = 0
        p = headB

        while p:
            m += 1
            p = p.next

        p1 = headA
        p2 = headB

        if n > m:
            for i in range(n - m):
                p1 = p1.next
        else:
            for i in range(m - n):
                p2 = p2.next

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1
            


        