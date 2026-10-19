class Solution(object):
    def findErrorNums(self, nums):
        hash = {}
        maxval = max(nums)
        lst = []        
        for ch in nums:
            if ch not in hash:
                hash[ch] = 1
            else:
                hash[ch] += 1
        for ch in nums:
            if hash[ch] == 2:
                lst.append(ch)     
                break    
        hashset = set(nums)
        for i in range(1,maxval+1):
            if i not in hashset:
                lst.append(i)
            else: 
                continue  
        if len(lst) == 1:
            lst.append(len(nums))                     
        return lst       