class Solution(object):
    def removeElement(self, nums, val):
        x=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[x]=nums[i]
                x=x+1
        return x
b=Solution()
val=3
nums=[3,2,2,3]
print(b.removeElement(nums,val))                
     