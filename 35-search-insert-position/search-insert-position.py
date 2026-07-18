class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        for i in range(len(nums)):
            if nums[i]>target:
                return i
        return len(nums)        


k=Solution()
nums=[1,3,5,6]
target=5
print(k.searchInsert(nums,target))               
    
        