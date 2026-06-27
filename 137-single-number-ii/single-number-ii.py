class Solution(object):
    def singleNumber(self, nums):
        hash={}
        for num in nums:
            if num not in hash:
                hash[num]=1
            else:
                hash[num]+=1
        for ch in hash:
            if hash[ch]==1:
                return ch
       