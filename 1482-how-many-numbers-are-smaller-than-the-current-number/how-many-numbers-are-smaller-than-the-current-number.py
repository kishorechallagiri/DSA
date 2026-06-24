class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        lst=[]
        for i in range(len(nums)):
            min_count=0
            for j in range(len(nums)):
                if nums[j]<nums[i]:
                    min_count+=1
            lst.append(min_count)
            min_count=0 
              
        return lst           
        