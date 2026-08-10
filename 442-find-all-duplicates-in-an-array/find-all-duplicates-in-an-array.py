class Solution(object):
    def findDuplicates(self, nums):
        hash={}
        lst=[]
        for ch in nums:
            if ch not in hash:
                hash[ch]=1
            else:
                hash[ch]+=1
        for ch in nums:
            if hash[ch]>1:
                if ch not in lst:
                    lst.append(ch)
        return lst        

        
        