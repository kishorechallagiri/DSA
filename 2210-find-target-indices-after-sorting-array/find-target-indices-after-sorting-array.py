class Solution(object):
    def targetIndices(self, nums, target):
        lst=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==target:
                lst.append(i)
             
        return lst         


       