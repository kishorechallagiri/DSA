class Solution(object):
    def sumOfSquares(self, nums):
        sumval = 0
        for i in range(len(nums)):
            if len(nums)%(i+1) == 0:
                sumval += nums[i]*nums[i]
        return sumval     