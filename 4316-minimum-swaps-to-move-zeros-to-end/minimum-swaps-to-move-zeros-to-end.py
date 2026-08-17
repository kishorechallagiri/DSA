class Solution(object):
    def minimumSwaps(self, nums):
        count=0
        left=0
        right=len(nums)-1
        while left<=right:
            if nums[left]==0:
                if nums[right]==0:
                    right-=1
                else:
                    nums[left],nums[right]=nums[right],nums[left]
                    count+=1
                    left+=1
                    right-=1
            else:
                left+=1
        return count            

        
        