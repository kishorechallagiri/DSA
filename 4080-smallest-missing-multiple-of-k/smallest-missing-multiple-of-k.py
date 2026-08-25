class Solution(object):
    def missingMultiple(self, nums, k):
        hash=set(nums)
        
        for i in range(1,len(nums)+2):
            mul=i*k
            if mul not in hash:
                    return mul
