class Solution(object):
    def majorityElement(self, nums):
        hash={}
        n=len(nums)//3
        lst=[]
        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]]=1
            else:
                hash[nums[i]]+=1  
        for ch in hash:
            if hash[ch]>n:
                lst.append(ch) 
        return lst                 

        