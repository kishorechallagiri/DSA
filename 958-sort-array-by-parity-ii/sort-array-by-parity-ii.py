class Solution(object):
    def sortArrayByParityII(self, nums):
        lst = [0]*len(nums)
        x = 0
        y = 1
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                lst[x] = nums[i]
                x+=2
        for j in range(len(nums)):
            if nums[j]%2 == 1:
                lst[y] = nums[j]
                y+=2
        return lst       
