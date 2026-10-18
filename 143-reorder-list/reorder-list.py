
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        stack = []
        curr = slow

        while curr:
            stack.append(curr.val)
            curr = curr.next

        # Disconnect the second half
        curr = head
        while curr.next != slow:
            curr = curr.next
        curr.next = None

        # Insert values from the stack
        curr = head

        while stack:
            val = stack.pop()
            temp = curr.next
            node = ListNode(val)
            curr.next = node
            node.next = temp
            curr = temp if temp else node

        return




        
        

        
        