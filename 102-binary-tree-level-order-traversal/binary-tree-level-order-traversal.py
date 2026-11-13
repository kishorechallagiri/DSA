# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []

        q = deque([root])
        ans = []

        while q:
            levelArr = []
            levelSize = len(q)

            for i in range(levelSize):
                curr = q.popleft()

                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)

                levelArr.append(curr.val)

            ans.append(levelArr)

        return ans
                


            


