class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        min_count=0
        max_count=0
        for i in range (len(nums)):
            if nums[i]==1:
                min_count+=1
            else:
                max_count=max(min_count,max_count)
                min_count=0
        return  max(min_count,max_count)           

        
        