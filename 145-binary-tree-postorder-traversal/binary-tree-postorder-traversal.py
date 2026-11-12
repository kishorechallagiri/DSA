# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        stack = []
        curr = root
        ans = []
        lastVisited = 0
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            peekNode = stack[len(stack)-1]
            if peekNode.right and peekNode.right != lastVisited:
                curr = peekNode.right
            else:
                ans.append(peekNode.val)  
                lastVisited = stack.pop()  
        return ans            