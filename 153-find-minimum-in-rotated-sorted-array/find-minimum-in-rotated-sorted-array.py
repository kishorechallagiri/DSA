class Solution(object):
    def findMin(self, nums):
        l,r=0,len(nums)-1
        
        while l<=r:
            if nums[l]<=nums[r]:
                return nums[l]
            m=l+(r-l)//2 
            if nums[m]<nums[m-1]:
                return nums[m] 
            #left half is nor sorted
            if nums[l]>nums[m]:
                r=m-1
            else:
                l=m+1           


        