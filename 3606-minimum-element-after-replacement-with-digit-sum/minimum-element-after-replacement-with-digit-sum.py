class Solution(object):
    def minElement(self, nums):
        lst=[]
        
        for ch in nums:
            count=0
            for i in str(ch):
                count+=int(i)

            lst.append(count)  
            count=0
        return min(lst)     