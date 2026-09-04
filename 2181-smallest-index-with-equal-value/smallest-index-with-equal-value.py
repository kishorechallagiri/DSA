class Solution(object):
    def smallestEqual(self, nums):
        minindex=float('inf')
        for i in range(len(nums)):
            if nums[i]==i%10:
                minindex=min(minindex,i)
        if minindex == float('inf'):
            return -1
        else:
            return minindex
        