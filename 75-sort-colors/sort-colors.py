class Solution(object):
    def sortColors(self, nums):
        n=len(nums)
        for i in range(n-1):
            is_swapped=False
            for j in range(n-1-i):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
                    is_swapped=True
            if not is_swapped:
                break
                        
        return nums                


        
        
        