from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def isSymmetric(self, root):

        if not root:
            return True

        q = deque([root.left, root.right])

        while q:
            p1 = q.popleft()
            p2 = q.popleft()

            if not p1 and not p2:
                continue

            if not p1 or not p2 or p1.val != p2.val:
                return False

            q.append(p1.left)
            q.append(p2.right)

            q.append(p1.right)
            q.append(p2.left)

        return True