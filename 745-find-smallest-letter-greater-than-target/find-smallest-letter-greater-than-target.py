class Solution(object):
    def nextGreatestLetter(self, nums, target):
        l=0
        r=len(nums)-1
        smallest = 0
        while l<=r:
            m=l+(r-l)//2
            if nums[m]>target:
                smallest = nums[m]
                r = m - 1
            elif target<nums[m]:
                r=m-1
            else:
                l=m+1
        if  smallest  :
            return smallest
        else:
            return nums[0]      