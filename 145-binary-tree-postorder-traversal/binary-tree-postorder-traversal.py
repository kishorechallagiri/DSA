# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []

        s1 = [root]
        s2 = []

        while s1:
            curr = s1.pop()
            s2.append(curr)

            if curr.left:
                s1.append(curr.left)

            if curr.right:
                s1.append(curr.right)

        ans = []

        while s2:
            ans.append(s2.pop().val)

        return ans