class Solution(object):
    def removeDuplicates(self, nums):
        x=0
        for i in range(len(nums)):
            if nums[i]>nums[x]:
                x=x+1
                nums[x]=nums[i]
        return x+1
b=Solution()
nums=[0,0,1,1,1,2,2,3,3,4]
print(b.removeDuplicates(nums))               
\