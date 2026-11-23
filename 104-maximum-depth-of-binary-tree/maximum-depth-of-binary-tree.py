# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        maxdepth = 0

        def traversal(curr, depth):
            nonlocal maxdepth

            if not curr:
                return

            maxdepth = max(maxdepth, depth)

            traversal(curr.left, depth + 1)
            traversal(curr.right, depth + 1)

        traversal(root, 1)
        return maxdepth
        