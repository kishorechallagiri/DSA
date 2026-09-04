class Solution(object):
    
    def smallestIndex(self, nums):
        val=0
        for i in range(len(nums)):
            for j in str(nums[i]):
                val+=int(j)
            if val==i:
                return i
            else:
                val=0    
        return -1            


        