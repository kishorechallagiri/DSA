class Solution(object):
    def minMoves(self, nums):
        count = 0
        maxval = max(nums)
        print(maxval)
        for i in range(len(nums)) :
            if nums[i]!=maxval :
                count += maxval - nums[i]
        return count        
                   
        
        