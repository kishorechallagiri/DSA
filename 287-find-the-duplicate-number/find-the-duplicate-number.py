class Solution(object):
    def findDuplicate(self, nums):
        hash={}
        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]]=1
            else:
                hash[nums[i]]+=1
        for ch in hash:
            if hash[ch]>=2:
                return ch            
        
        