class Solution(object):
    def singleNumber(self, nums):
        xor = 0
        for ch in nums:
            xor = xor^ch
        return xor    
        
        