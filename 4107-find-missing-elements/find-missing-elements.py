class Solution(object):
    def findMissingElements(self, nums):
        nums_set=set(nums)
        first,last=min(nums),max(nums)
        return [i for i in range(first,last+1) if i not in nums_set]
       


        