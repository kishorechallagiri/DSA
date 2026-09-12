class Solution(object):
    def pivotIndex(self, nums):
        for i in range(len(nums)):
            left = nums[:i]
            right = nums[i+1:]
            if sum(left) == sum(right):
                return i
        return -1