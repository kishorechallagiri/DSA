class Solution(object):
    def searchRange(self, nums, target):
        l=0
        r=len(nums)-1
        ans=-1
        lst=[]
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                ans=mid
                r=mid-1
            elif target<nums[mid]:

                r=mid-1
            else:
                l=mid+1      
        lst.append(ans)
        l=0
        r=len(nums)-1
        mid=-1        
        while l<=r:
            m=l+(r-l)//2
            if nums[m]==target:
                mid=m
                l=m+1
                
            elif target<nums[m]:
                r=m-1
            else:
                l=m+1    
        lst.append(mid)       
        return lst