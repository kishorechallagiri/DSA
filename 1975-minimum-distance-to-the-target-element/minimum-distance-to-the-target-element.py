class Solution(object):
    def getMinDistance(self, nums, target, start):
        minval=float('inf')
        for i in range(len(nums)):
            if nums[i]==target:
                minval = min(abs(i-start),minval)
        return minval