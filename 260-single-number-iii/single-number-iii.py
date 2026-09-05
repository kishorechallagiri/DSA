class Solution(object):
    def singleNumber(self, nums):
        hash={}
        for ch in nums:
            if ch not in hash:
                hash[ch]=1
            else:
                hash[ch]+=1
        lst=[]        
        for ch in nums:
            if hash[ch]==1:
                lst.append(ch)
        return lst        

                
        