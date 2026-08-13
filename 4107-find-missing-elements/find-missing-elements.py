class Solution(object):
    def findMissingElements(self, nums):
        nums.sort()
        lst=[]
        hash=set(nums)
        first=nums[0]
        last=nums[-1]
        for i in range(first,last+1):
            if i not in hash:
                lst.append(i)
            
        return lst        


        