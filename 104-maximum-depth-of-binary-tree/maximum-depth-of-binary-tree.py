# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        maxdepth = [0]

        def traversal(curr, depth):
            if not curr:
                return

            maxdepth[0] = max(maxdepth[0], depth)

            traversal(curr.left, depth + 1)
            traversal(curr.right, depth + 1)

        traversal(root, 1)
        return maxdepth[0]
        