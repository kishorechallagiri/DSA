class Solution(object):
    def searchInsert(self, nums, target):
        l=0
        r=len(nums)-1
        while l<=r:
            m=l+(r-l)//2
            if nums[m]==target:
                return m
            elif target<nums[m]:
                r=m-1
            else:
                l=m+1
        return l                        # Write your solution here
